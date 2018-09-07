
class FormData():
    def create_preprints(self, nodes, file_id):
        data = {}

        node = {}
        node_data = {}
        node_data['data'] = {"type": "nodes", "id": nodes}  # osf repo id
        file_data = {}
        file_data['data'] = {"type": "files", "id": file_id}
        provider_data = {}
        provider_data['data'] = {"type": "providers", "id": "osf"}

        node['node'] = node_data
        node['primary_file'] = file_data
        node['provider'] = provider_data
        data['relationships'] = node

        data['attributes'] = {"provider": "osf", "primary_file": file_id, "subjects": []}

        data['type'] = "preprints"
        samdasu = {}
        samdasu['data'] = data
        return samdasu

    def create_preprints_patch(self, preprints_id, p_year_month, po, abstract, doi):
        data = {}
        attributes = {}
        attributes['description'] = abstract
        attributes['doi'] = doi
        attributes['original_publication_date'] = p_year_month
        license_record = {}
        license_record['copyright_holders'] = [po]
        license_record['year'] = 2018
        attributes['license_record'] = license_record

        node = {}
        license = {}
        license_data = {}
        license_data['id'] = '5b5846f86c9f6b0001869342'
        license_data['type'] = 'licenses'
        license['data'] = license_data
        provider_data = {}
        provider_data['data'] = {"type": "providers", "id": "osf"}
        node['provider'] = provider_data
        node['license'] = license
        data['relationships'] = node
        data['attributes'] = attributes

        data['type'] = "preprints"
        data['id'] = preprints_id
        samdasu = {}
        samdasu['data'] = data
        return samdasu

    def create_preprints_patch_category(self, preprints_id, subject_list):
        data = {}
        attributes = {}
        attributes['subjects'] = [subject_list]

        provider_data = {}
        provider_data['data'] = {"type": "providers", "id": "osf"}
        node = {}
        node['provider'] = provider_data
        data['relationships'] = node
        data['attributes'] = attributes

        data['type'] = "preprints"
        data['id'] = preprints_id
        samdasu = {}
        samdasu['data'] = data
        return samdasu

    def create_contributor(self, user_id):
        samdas = {}
        data = {}
        attributes = {}
        attributes['bibliographic'] = True
        attributes['permission'] = 'write'
        attributes['send_email'] = False
        data['attributes'] = attributes
        relationships = {}
        users = {}
        users_data = {}
        users_data['id'] = user_id
        users_data['type'] = 'users'
        users['data'] = users_data
        relationships['users'] = users
        data['relationships'] = relationships
        data['type'] = 'contributors'
        samdas['data'] = data
        return samdas

    def create_nodes(self, title):
        data = {}
        node = {}
        node['type'] = "nodes"
        node['attributes'] = {"title": title, "category": "project", "public": True}
        node['relationships'] = {}
        data['data'] = node
        return data

    def create_published(self, id):
        samdasu = {}
        data = {}
        attributes = {}
        attributes['is_published'] = True
        relationships = {}
        provider = {}
        provider['data'] = {'id':'osf','type':'providers'}
        relationships['provider'] = provider
        data['id'] = id
        data['attributes'] = attributes
        data['relationships'] = relationships
        data['type'] = 'preprints'
        samdasu['data'] = data
        return samdasu

    def create_user(self, email, fullname, password):
        datas = {}
        datas['acceptedTermsOfService'] = True
        datas['campaign'] = ''
        datas['email1'] = email
        datas['email2'] = email
        datas['errors'] = []
        datas['fullName'] = fullname
        datas['isValid'] = True
        datas['message'] = ''
        datas['messageClass'] = 'text-info'
        datas['password'] = password
        return datas

    def create_contributors_form(self, contributor_datum):
        contributor_list = []
        for c_data in contributor_datum:
            contributors = {}
            c_attributes = c_data.get('embeds').get('users').get('data').get('attributes')
            c_id = c_data.get('id')
            c_user_id = c_data.get('embeds').get('users').get('data').get('id')
            c_type = 'person'
            c_name = c_attributes.get('full_name')
            c_given_name = c_attributes.get('given_name')
            c_family_name = c_attributes.get('family_name')
            c_identifiers = 'http://localhost:5000/{}/'.format(c_user_id)
            c_order_cited = c_data.get('attributes').get('index')
            c_cited_as = c_name
            c_affiliations = []
            c_award = []
            c_types = ['person', 'agent']
            c_relation = 'creator'
            contributors['id'] = c_id
            contributors['type'] = c_type
            contributors['name'] = c_name
            contributors['given_name'] = c_given_name
            contributors['family_name'] = c_family_name
            contributors['identifiers'] = [c_identifiers]
            contributors['order_cited'] = c_order_cited
            contributors['cited_as'] = c_cited_as
            contributors['affiliations'] = c_affiliations
            contributors['awards'] = c_award
            contributors['types'] = c_types
            contributors['relation'] = c_relation
            contributor_list.append(contributors)
        return contributor_list

    def create_publishers_form(self):
        publishers_list = []
        publisher = {}
        publisher['id'] = '64155-6D7-742'
        publisher['type'] = 'institution'
        publisher['name'] = 'Center for Open Science'
        publisher['identifiers'] = []
        publisher['cited_as'] = ''
        publisher['affiliations'] = []
        publisher['awards'] = []
        publisher['types'] = ['institution', 'organization', 'agent']
        publisher['relation'] = 'publisher'
        publishers_list.append(publisher)
        return publishers_list

    def create_preprints_form(self):
        preprints = {}
        preprints['type'] = 'preprints'
        preprints['language'] = None
        preprints['registration_type'] = None
        preprints['withdrawn'] = None
        preprints['justification'] = None
        preprints['tags'] = []
        preprints['sources'] = ['CrossRef', 'OSF']
        preprints['subject_synonyms'] = []
        preprints['affiliations'] = []
        preprints['retracted'] = False
        preprints['types'] = ['preprint', 'publication', 'creative work']
        return preprints


