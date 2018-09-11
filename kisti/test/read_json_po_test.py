import json
import io
from osf import subject

gs = subject.Subject()

with io.open('/home/samdasu/PycharmProjects/kci/osf/json/kci_paper_po.json', 'r') as f:
    data = json.load(f)


for i in data:
    print(i, gs.get_subject(i))
