import json
import requests
from requests.auth import HTTPBasicAuth


def request_preprints_list(id):
    url = 'http://localhost:8000/v2/preprints/{}/'.format(id)
    r = requests.get(url, auth=HTTPBasicAuth('cbal@li-st.com', ''))
    if r.status_code < 300:
        return json.loads(r.text)
    elif r.status_code == 404:
        return 0
    else:
        return json.loads(r.text)


data = request_preprints_list('etdna')
print(data)
data = request_preprints_list('5d3au')
print(data)

