import requests
import io
from requests.auth import HTTPBasicAuth
import os


class CreateFile():

    def request_newfile(self, email, nodes):
        file_data = self.read_pdf()
        # nodes = "q4n7t"
        filename = "test_preprints.pdf"
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:7777/v1/resources/{0}/providers/osfstorage/?kind=file&name={1}'.format(nodes, filename)
        r = requests.put(url, data=file_data, auth=HTTPBasicAuth(email, ''), headers=headers)
        return r


    def read_pdf(self):
        HERE = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(HERE, 'test_preprints.pdf')
        with io.open(file_path, 'rb') as f:
            result = f.read()
        return result


