import unittest
from osf import read_json


class CreateUser(unittest.TestCase):
    def test(self):
        value = 'jino.kor@li-st.com'
        value = value.split('@', 1)[0]
        self.assertEqual(value, 'jino.kor')
        self.assertTrue(True)

    def test_read_json(self):
        rj = read_json.ReadJson()
        data = rj.get_library()
        self.assertTrue(len(data) > 0)

    def test_view_json(self):
        rj = read_json.ReadJson()
        data = rj.read_json('./json/kci_paper_library_one.json')
        print(data)

    def test_get_author(self):
        rj = read_json.ReadJson()
        author_main = []
        datas = rj.get_library()
        for data in datas:
            author_main.append(data.get('AUTHOR_MAIN'))
            temp = data.get('AUTHOR_SUB')
            if temp is not None:
                ss = temp.split(';')
                for j in ss:
                    author_main.append(j)
        author_main = sorted(list(set(author_main)))
        self.assertTrue(len(author_main) > 0)


if __name__ == '__main__':
    unittest.main()
