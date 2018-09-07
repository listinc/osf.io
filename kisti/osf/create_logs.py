import requests
from requests.auth import HTTPBasicAuth
import json


def action_preprints():
    url = "http://localhost:8000/v2/actions/requests/preprints/"
    samdas = {}
    data = {}
    data['attributes'] = {"trigger":"trigger"}
    data['relationships'] = {"target":"preprints", "provider":"osf", "creator":""}
    data['links'] = {"self":""}
    data['embeds'] = {}
    data['id'] = ''
    data['type'] = 'logs'
    samdas['data'] = data
    headers = {'content-type': 'application/json'}
    request_data = json.dumps(samdas)
    print(request_data)
    r = requests.post(url, request_data, auth=HTTPBasicAuth('cbal@li-st.com', ''), headers=headers)
    print(r.text)


action_preprints()