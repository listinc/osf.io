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
            author_main.append(data.get('AUTHOR_MAIN'))
            temp = data.get('AUTHOR_SUB')
            if temp is not None:
                ss = temp.split(';')
                for j in ss:
                    author_main.append(j)
        author_main = sorted(list(set(author_main)))
        return author_main[1:]

    def get_library(self):
        file_name = './json/kci_paper_library_one.json'
        return self.read_json(file_name)

    def read_failed_contributor(self):
        data = []
        HERE = os.path.dirname(os.path.abspath(__file__))
        text_path = os.path.join(HERE, 'json/failed_contributor.txt')
        with io.open(text_path, 'r') as f:
            line = f.readlines()
            data.append(line)
        return data
