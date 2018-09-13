import unittest
from osf import read_json
import collections


class AuthorTest(unittest.TestCase):
    def test_get_author(self):
        rj = read_json.ReadJson()
        datas = rj.read_json('./json/kci_paper_library_one.json')
        author_list = rj.get_author(datas)
        self.assertTrue('유영준' in author_list)

    def test_create_email(self):
        rj = read_json.ReadJson()
        data = rj.read_json('./json/kci_paper_library_one.json')
        author_list = rj.get_author(data)

        for index, author in enumerate(author_list):
            author_list[index] = author.replace(';', '')
        author_list = list(set(author_list))
        samdasu = {}
        for index, author in enumerate(sorted(author_list)):
            email = 'ksim{0}@gmail.com'.format(index)
            samdasu[author] = email

        samdasu = collections.OrderedDict(sorted(samdasu.items()))
        self.assertEqual("ksim359@gmail.com", samdasu.get('유영준'))


if __name__ == '__main__':
    unittest.main()
