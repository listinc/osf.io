import requests
import io
from requests.auth import HTTPBasicAuth
import os


class CreateFile():
    def read_pdf(self, file_name):
        HERE = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(HERE, './pdf/{}'.format(file_name))
        with io.open(file_path, 'rb') as f:
            result = f.read()
        return result


