import unittest
from osf import read_json


class CreateUser(unittest.TestCase):
    def test_contributors_data(self):
        rj = read_json.ReadJson()
        data = rj.read_failed_contributor()
        obj = data[0].split(' ')
        user_id = obj[2]
        preprint_id = obj[3]
        print(obj[2])
        print(ojb[3])
        self.assertEqual(user_id, 'tq35m')
