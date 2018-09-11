from osf import read_json
from osf import request


rj = read_json.ReadJson()
datas = rj.read_json('kci_paper.json')
author = rj.read_json('author_email_mapping.json')
create_contributor = request.RequestPreprints()
for data in datas:
    author_main = data.get("author_main")
    author_sub = data.get("author_sub")
    if author_sub is not None:
        result = author_sub.split(";")
        for name in result:
            print("sub", author.get(name))
    print("main", author.get(author_main))



