import unittest
import json
import requests
from requests.auth import HTTPBasicAuth


class TestRequestPreprintsList(unittest.TestCase):
    def test_request_preprints_list(self):
        url = 'http://localhost:8000/v2/preprints/?page={}'.format(1)
        r = requests.get(url, auth=HTTPBasicAuth('cbal@li-st.com', ''))
        datum = json.loads(r.text)

        self.assertTrue(len(datum) > 0)


if __name__ == '__main__':
    unittest.main()
