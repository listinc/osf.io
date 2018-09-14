import io
import json
import itertools
from osf import read_json


rj = read_json.ReadJson()
data = rj.read_json('./json/author_email_mapping.json')

author_main = []
author_sub = []
for i in data:
    author_main.append(i.get('author_main'))
    temp = i.get('author_sub')
    if temp is not None:
        ss = temp.split(';')

        for j in ss:
            author_sub.append(j)

count= 0
for k, v in itertools.groupby(sorted(author_main)):
    samdasu = list(v)
    if len(samdasu) > 0:
        count += 1

count2 = 0
for k, v in itertools.groupby(sorted(author_sub)):
    samdasu = list(v)
    if len(samdasu) > 0:
        count2 += 1
count3 = 0
author_total = author_main+author_sub
for k, v in itertools.groupby(sorted(author_total)):
    samdasu = list(v)
    if len(samdasu) > 0:
        count3 += 1

print(len(data))
print(count)
print(count2)
print(count3)