import requests
from requests.auth import HTTPBasicAuth
import json


class PatchContributors():
    def patch_contributors(self, email, nodes_id, contributor_data):
        url = "http://localhost:8000/v2/nodes/{}/contributors/?embed=node&send_email=false".format(nodes_id)
        data = json.dumps(contributor_data)
        headers = {'content-type': 'application/json'}
        r = requests.patch(url, data, auth=HTTPBasicAuth(email, ''), headers=headers)
        return r


# pc = PatchContributors()
# pc.patch_contributors('cbal@li-st.com', 'q4n7t', '3sfx6')
