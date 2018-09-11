from osf import read_json

def read_kci_paper():
    rj = read_json.ReadJson()
    data = rj.read_json('json/kci_paper.json')

    for i in data:
        if i.get('author_main') == '오삼균':
            print(i)


def read_author():
    rj = read_json.ReadJson()
    data = rj.read_json('json/author_email_mapping.json')
    print(data.get('홍재현'))


def read_title():
    rj = read_json.ReadJson()
    data = rj.read_json('json/kci_paper.json')
    for i in data:
        if i.get('title01') == '국내 학술지 논문의 오픈 액세스와 아카이빙을 위한 저작권 귀속 연구: 한국학술진흥재단 등재 학술지를 중심으로':
            print(i)


def read_po():
    rj = read_json.ReadJson()
    data = rj.read_json('json/kci_paper.json')
    for i in data:
        print(i.get('po'))


def read_po_condition():
    rj = read_json.ReadJson()
    data = rj.read_json('json/kci_paper.json')
    count = 0
    author_list = []
    print(len(data))
    for i in data:
        if i.get('po') == '한국정보관리학회':
            author_list.append(i.get('author_main'))
            count+=1

    print(count)
    print(len(author_list))
    author_list = list(set(author_list))
    print(sorted(author_list))
    print(len(author_list))


if __name__ == '__main__':
    read_po_condition()
