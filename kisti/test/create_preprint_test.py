import unittest
from osf import request


class CreatePreprints(unittest.TestCase):
    def test(self):
        cp = request.RequestPreprints()
        r = cp.request_user('cbal@li-st.com')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
