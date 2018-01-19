from nose.tools import *  # flake8: noqa
import mock
import pytest
from framework.auth import Auth

from api.base.settings.defaults import API_BASE

from tests.base import ApiWikiTestCase
from osf_tests.factories import ProjectFactory, RegistrationFactory


class TestWikiVersionContentView(ApiWikiTestCase):

    def _set_up_public_project_with_wiki_page(self):
        self.public_project = ProjectFactory(is_public=True, creator=self.user)
        self.public_wiki = self._add_project_wiki_version(self.public_project, self.user)
        self.public_url = '/{}wiki_versions/{}/content/'.format(API_BASE, self.public_wiki._id)

    def _set_up_private_project_with_wiki_page(self):
        self.private_project = ProjectFactory(creator=self.user)
        self.private_wiki = self._add_project_wiki_version(self.private_project, self.user)
        self.private_url = '/{}wiki_versions/{}/content/'.format(API_BASE, self.private_wiki._id)

    def _set_up_public_registration_with_wiki_page(self):
        self._set_up_public_project_with_wiki_page()
        self.public_registration = RegistrationFactory(project=self.public_project, user=self.user, is_public=True)
        self.public_registration_wiki_id = self.public_registration.get_wiki_version('home')._id
        self.public_registration.save()
        self.public_registration_url = '/{}wiki_versions/{}/content/'.format(API_BASE, self.public_registration_wiki_id)

    def test_logged_out_user_can_get_public_wiki_content(self):
        self._set_up_public_project_with_wiki_page()
        res = self.app.get(self.public_url)
        assert_equal(res.status_code, 200)
        assert_equal(res.content_type, 'text/markdown')
        assert_equal(res.body, self.public_wiki.content)

    def test_logged_in_non_contributor_can_get_public_wiki_content(self):
        self._set_up_public_project_with_wiki_page()
        res = self.app.get(self.public_url, auth=self.non_contributor.auth)
        assert_equal(res.status_code, 200)
        assert_equal(res.content_type, 'text/markdown')
        assert_equal(res.body, self.public_wiki.content)

    def test_logged_in_contributor_can_get_public_wiki_content(self):
        self._set_up_public_project_with_wiki_page()
        res = self.app.get(self.public_url, auth=self.user.auth)
        assert_equal(res.status_code, 200)
        assert_equal(res.content_type, 'text/markdown')
        assert_equal(res.body, self.public_wiki.content)

    def test_logged_out_user_cannot_get_private_wiki_content(self):
        self._set_up_private_project_with_wiki_page()
        res = self.app.get(self.private_url, expect_errors=True)
        assert_equal(res.status_code, 401)

    def test_logged_in_non_contributor_cannot_get_private_wiki_content(self):
        self._set_up_private_project_with_wiki_page()
        res = self.app.get(self.private_url, auth=self.non_contributor.auth, expect_errors=True)
        assert_equal(res.status_code, 403)

    def test_logged_in_contributor_can_get_private_wiki_content(self):
        self._set_up_private_project_with_wiki_page()
        res = self.app.get(self.private_url, auth=self.user.auth)
        assert_equal(res.status_code, 200)
        assert_equal(res.content_type, 'text/markdown')
        assert_equal(res.body, self.private_wiki.content)

    def test_older_versions_content_can_be_accessed(self):
        self._set_up_private_project_with_wiki_page()
        # Create a second version
        wiki_page, wiki_version = self.private_project.create_or_update_node_wiki(self.private_wiki.wiki_page.page_name, 'Second draft of wiki', Auth(self.user))

        res = self.app.get(self.private_url, auth=self.user.auth)
        assert_equal(res.status_code, 200)
        assert_equal(res.content_type, 'text/markdown')
        assert_equal(res.body, self.private_wiki.content)

        self.private_url_latest = '/{}wiki_versions/{}/content/'.format(API_BASE, wiki_version._id)
        res = self.app.get(self.private_url_latest, auth=self.user.auth)
        assert_equal(res.status_code, 200)
        assert_equal(res.content_type, 'text/markdown')
        assert_equal(res.body, wiki_version.content)

    def test_user_cannot_get_withdrawn_registration_wiki_content(self):
        self._set_up_public_registration_with_wiki_page()
        withdrawal = self.public_registration.retract_registration(user=self.user, save=True)
        token = withdrawal.approval_state.values()[0]['approval_token']
        withdrawal.approve_retraction(self.user, token)
        withdrawal.save()
        res = self.app.get(self.public_registration_url, auth=self.user.auth, expect_errors=True)
        assert_equal(res.status_code, 403)
