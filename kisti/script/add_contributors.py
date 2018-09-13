from osf import request
from osf import formdata
from osf import connection
from osf import read_json

def add_contributors():
    """
    1. select object_id from osf_guid where _id = 'xunvr';
    2. select node_id from osf_preprintservice where id = '46'
    3. select _id from osf_guid where object_id = 708;
    select _id from osf_guid where object_id = (select node_id from osf_preprintservice where id = (select object_id from osf_guid where _id = 'xunvr'));

    1. select object_id from osf_guid where _id = 'xunvr';
    2. select node_id from osf_preprintservice where id = 46;
    3. select creator_id from osf_abstractnode where id = 708;
    4. select username from osf_osfuser where id = 564;
    select username from osf_osfuser where id = (select creator_id from osf_abstractnode where id = (select node_id from osf_preprintservice where id = (select object_id from osf_guid where _id = 'xunvr')))


    """

    rp = request.RequestPreprints()
    rj = read_json.ReadJson()
    fm = formdata.FormData()
    data = rj.read_failed_contributor()
    cursor = connection.OSFDB()
    curs = cursor.connect()
    for i in data:
        print(i)
        obj = i[0].split(' ')
        user_id = obj[2]
        preprint_id = obj[3]

        sql_get_node_id = "select _id from osf_guid where object_id = " \
                          "(select node_id from osf_preprintservice where id = " \
                          "(select object_id from osf_guid where _id = '{}'))".format(preprint_id)

        sql_get_username = "select username from osf_osfuser where id = " \
                           "(select creator_id from osf_abstractnode where id = " \
                           "(select node_id from osf_preprintservice where id = " \
                           "(select object_id from osf_guid where _id = '{}')))".format(preprint_id)

        curs.execute(sql_get_node_id)
        nodes_id = curs.fetchone()[0]

        curs.execute(sql_get_username)
        email = curs.fetchone()[0]
        # user_id = 'tq35m'

        contributor_data = fm.create_contributor(user_id)
        print(contributor_data)
        if nodes_id is not None and email is not None:
            r = rp.patch_contributors(email, nodes_id, contributor_data)
            print(r.text, r.status_code, email, nodes_id, user_id)
        break

    cursor.close(curs)


add_contributors()