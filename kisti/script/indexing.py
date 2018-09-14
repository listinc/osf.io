import json
import time
from osf import request
from osf import formdata


start_time = time.time()
rp = request.RequestPreprints()
fm = formdata.FormData()
for i in range(1, 100):
    if i > 2:
        break
    r = rp.request_preprints_list(i)
    if r.status_code < 300:
        datum = json.loads(r.text)
    elif r.status_code == 404:
        datum = 0
        break
    else:
        datum = json.loads(r.text)

    for data in datum.get('data'):
        preprint = {}

        preprint_form = fm.create_preprints_form()
        preprint.update(preprint_form)
        id = data.get('id')
        preprint['id'] = id
        attributes = data.get('attributes')
        preprint['title'] = attributes.get('title')
        preprint['description'] = attributes.get('description')
        preprint['date_created'] = attributes.get('date_created') + "+00:00"
        preprint['date_modified'] = attributes.get('date_created') + "+00:00"
        preprint['date_updated'] = attributes.get('date_created') + "+00:00"
        preprint['date_published'] = attributes.get('date_created') + "+00:00"
        relationships = data.get('relationships')
        subjects = attributes.get('subjects')
        subjects_result = []
        for i in subjects:
            value = "bepress"
            for j in i:
                value = value + "|" + j.get('text')
            subjects_result.append(value)

        preprint['subjects'] = subjects_result
        contributor_url = relationships.get('contributors').get('links').get('related').get('href')

        r = rp.request_contributors(contributor_url)

        if r.status_code < 300:
            contributor_datum = json.loads(r.text)
        else:
            print("contributors not found ", r.status_code, r.text)
        contributors_form = fm.create_contributors_form(contributor_datum.get('data'))
        publishers_form = fm.create_publishers_form()
        lists = {}
        lists['publishers '] = publishers_form
        lists['contributors'] = contributors_form

        preprint['lists'] = lists
        preprint['publishers'] = ['Center for Open Science']
        preprint['identifiers'] = ['http://112.218.235.198:5000/{}/'.format(id)]
        contributor_list = []
        for key in contributors_form:
            contributor_list.append(key.get('name'))

        preprint['contributors'] = contributor_list
        preprint['date'] = attributes.get('date_created') + "+00:00"

        # print(json.dumps(preprint))
        r = rp.request_indexing(json.dumps(preprint), id)
        if r.status_code > 299:
            print('error with : ' + id)
        else:
            print('created : '+id)


print("user created in --- %s seconds ---" % (time.time() - start_time))


