import io
import json
import os


class ReadJson():
    def read_json(self, file_name):
        HERE = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(HERE, file_name)
        with io.open(json_path, 'r') as f:
            data = json.load(f)
        return data

    def get_author(self, datas):
        author_main = []
        for data in datas:
            author_main.append(data.get('author_main'))
            temp = data.get('author_sub')
            if temp is not None:
                ss = temp.split(';')
                for j in ss:
                    author_main.append(j)
        author_main = sorted(list(set(author_main)))
        return author_main[1:]


