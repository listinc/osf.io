import requests
import json
from requests.auth import HTTPBasicAuth


class RequestPreprints():
    def __init__(self):
        self.host = '112.218.235.198'

    def request_preprints(self, email, preprints_data):
        headers = {'content-type': 'application/json'}
        url = 'http://{}:8000/v2/preprints/'.format(self.host)
        r = requests.post(url, data=json.dumps(preprints_data), auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def request_nodes(self, email, nodes_data):
        headers = {'content-type': 'application/json'}
        url = 'http://{}:8000/v2/nodes/'.format(self.host)
        r = requests.post(url, data=json.dumps(nodes_data), auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def patch_preprints(self, email, preprints_id, preprints_data):
        headers = {'content-type': 'application/json'}
        url = 'http://{}:8000/v2/preprints/{}/'.format(self.host, preprints_id)
        r = requests.patch(url, data=json.dumps(preprints_data), auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def request_user(self, email):
        headers = {'content-type': 'application/json'}
        url = 'http://{}:8000/v2/users/me/'.format(self.host)
        r = requests.get(url, auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def request_newfile(self, email, nodes, file_name, file_data):
        headers = {'content-type': 'application/json'}
        url = 'http://{0}:7777/v1/resources/{1}/providers/osfstorage/?kind=file&name={2}'.format(self.host, nodes, file_name)
        r = requests.put(url, data=file_data, auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def confirm_user(self, id, confirm_id):
        separator = '/'
        url = 'http://{}:5000/confirm/'.format(self.host)
        url = url + id + separator + confirm_id + separator
        r = requests.get(url)
        return r

    def create_user(self, datas):
        url = 'http://{}:5000/api/v1/register/'.format(self.host)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(datas), headers=headers)
        return r

    def patch_contributors(self, email, nodes_id, contributor_data):
        url = "http://{}:8000/v2/nodes/{}/contributors/?embed=node&send_email=false".format(self.host, nodes_id)
        data = json.dumps(contributor_data)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data, auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    #indexing
    def request_indexing(self, data, id):
        url = 'http://{}:9200/share_customtax_1/creativeworks/{}'.format(self.host, id)
        r = requests.put(url, data=data, headers={'content-type': 'application/json'})
        # print(r.text)
        return r

    def request_preprints_list(self, page):
        url = 'http://{}:8000/v2/preprints/?page={}'.format(self.host, page)
        r = requests.get(url, auth=HTTPBasicAuth('cbal@li-st.com', ''))
        return r

    def request_contributors(self, url):
        r = requests.get(url, auth=HTTPBasicAuth('cbal@li-st.com', ''))
        return r
