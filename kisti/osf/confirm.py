import psycopg2
import psycopg2.extras
from osf import request


def confirm_user():
    cp = request.RequestPreprints()
    conn_string = "host='localhost' dbname='osf' user='postgres'"

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    sql_string = "select id, email_verifications from osf_osfuser order by id desc"
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
            r = cp.confirm_user(guid, confirm_id)
            if r.status_code > 299:
                print(url, r.status_code)

    conn.commit()
    print("done: confirm_all_user")

