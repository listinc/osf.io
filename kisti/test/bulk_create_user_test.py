import unittest


class CreateUser(unittest.TestCase):
    def test(self):
        value = 'jino.kor@li-st.com'
        value = value.split('@', 1)[0]
        self.assertEqual(value, 'jino.kor')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
