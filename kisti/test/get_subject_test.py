import psycopg2
import psycopg2.extras
import unittest
from osf import subject


def get_data():
    conn_string = "host='localhost' dbname='osf' user='postgres'"

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    sql_string = "select text from osf_osfsubject"
    cursor.execute(sql_string)
    users = cursor.fetchall()

    for key in users:
        id = key.get('id')
        confirm_id = None
        for verification in key['email_verifications']:
            confirm_id = verification

        if confirm_id is not None:
            sql_string = "select _id from osf_guid where object_id={} and content_type_id=32".format(id)
            cursor.execute(sql_string)
            samdasu2 = cursor.fetchone()
            guid = samdasu2.get('_id')
            bulk_confirm_user.confirm_user(guid, confirm_id)

    conn.commit()
    print("done: confirm_all_user")

class CreateUser(unittest.TestCase):
    def test_subject_(self):
        library = ['한국기록관리학회', '한국기록학회', '한국도서관·정보학회', '한국문헌정보학회', '한국비블리아학회', '한국서지학회', '한국정보관리학회']
        po = '한국정보관리학회'
        if po in library:
            self.assertTrue(True)
    def test_subject_form(self):
        sj = subject.Subject()
        data = sj.get_subject('한국정보관리학회')
        self.assertEqual(['5b584937cd0fb400014752ba', '5b584937cd0fb400014752cd'], data)


