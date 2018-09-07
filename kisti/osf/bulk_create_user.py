import collections
from osf import read_json
from osf import formdata
from osf import request


def create_user_execute():
    fm = formdata.FormData()
    rp = request.RequestPreprints()
    data = create_user_email_dict()

    for key, value in data.items():
        datas = fm.create_user(value, key, value.rstrip('@gmail.com'))
        r = rp.create_user(datas)
        if r.status_code > 300:
            print(r.status_code, datas.get('email'))
    print("done: create_dummy_user")


def create_user_email_dict():
    rj = read_json.ReadJson()
    data = rj.read_json('./json/kci_paper.json')
    author_list = rj.get_author(data)

    for index, author in enumerate(author_list):
        author_list[index] = author.replace(';', '')
    author_list = list(set(author_list))
    samdasu = {}
    for index, author in enumerate(sorted(author_list)):
        email = 'kisti{0}@gmail.com'.format(index)
        samdasu[author] = email

    samdasu = collections.OrderedDict(sorted(samdasu.items()))
    return samdasu

