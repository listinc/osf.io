import requests
import json
from requests.auth import HTTPBasicAuth


class RequestPreprints():
    def request_preprints(self, email, preprints_data):
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:8000/v2/preprints/'
        r = requests.post(url, data=json.dumps(preprints_data), auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def request_nodes(self, email, nodes_data):
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:8000/v2/nodes/'
        r = requests.post(url, data=json.dumps(nodes_data), auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def patch_preprints(self, email, preprints_id, preprints_data):
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:8000/v2/preprints/{}/'.format(preprints_id)
        r = requests.patch(url, data=json.dumps(preprints_data), auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def request_user(self, email):
        headers = {'content-type': 'application/json'}
        r = requests.get('http://localhost:8000/v2/users/me/', auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    def get_json_id(self, data):
        data = json.loads(data)
        id = data.get("data").get("id")
        return id

    def get_files_id(self, data):
        data = json.loads(data)
        id = data.get('data').get('id')
        return id.lstrip("osfstorage/")

    def confirm_user(self, id, confirm_id):
        separator = '/'
        url = 'http://localhost:5000/confirm/'
        url = url + id + separator + confirm_id + separator
        r = requests.get(url)
        return r

    def create_user(self, datas):
        url = 'http://localhost:5000/api/v1/register/'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(datas), headers=headers)
        return r

    def patch_contributors(self, email, nodes_id, contributor_data):
        url = "http://localhost:8000/v2/nodes/{}/contributors/?embed=node&send_email=false".format(nodes_id)
        data = json.dumps(contributor_data)
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, data, auth=HTTPBasicAuth(email, ''), headers=headers)
        return r

    #indexing
    def request_indexing(self, data, id):
        url = 'http://localhost:9200/share_customtax_1/creativeworks/{}'.format(id)
        r = requests.put(url, data=data, headers={'content-type': 'application/json'})
        # print(r.text)
        return r

    def request_preprints_list(self, page):
        url = 'http://localhost:8000/v2/preprints/?page={}'.format(page)
        r = requests.get(url, auth=HTTPBasicAuth('cbal@li-st.com', ''))
        return r

    def request_contributors(self, url):
        r = requests.get(url, auth=HTTPBasicAuth('cbal@li-st.com', ''))
        return r