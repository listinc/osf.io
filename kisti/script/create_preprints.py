from osf import read_json
from osf import request as cp
from osf import create_file as cf
from osf import formdata
from osf import kci_util
from osf import subject
from osf import users
from osf import data_object
import time


if __name__ == '__main__':
    start_time = time.time()
    rj = read_json.ReadJson()
    datas = rj.read_json('./json/kci_paper.json')
    author = users.create_user_email_dict()
    create_preprints = cp.RequestPreprints()
    create_file = cf.CreateFile()
    fm = formdata.FormData()
    gs = subject.Subject()
    count = 0
    for data in datas:
        # /test/
        if count > 0:
            print("1 created in --- %s seconds ---" % (time.time() - start_time))
            break
        count += 1
        title01 = data.get("title01")
        print(title01)
        author_main = data.get("author_main")
        author_sub = data.get("author_sub")
        p_year_month = data.get("p_year_month")
        po = data.get("po")
        abstract = data.get("abstract")
        url = data.get("url")
        doi = data.get("doi")
        if doi is not None:
            doi = doi.lstrip("http://dx.doi.org/")
        email = author.get(author_main)
        if email is None:
            print("not found email", author_main)
            continue
        #get user id
        user_data = create_preprints.request_user(email)
        user_id = data_object.get_json_id(user_data.text)
        if user_id is None:
            print("user not found:", email)
        #create node
        nodes_data = fm.create_nodes(title01)
        nodes_data = create_preprints.request_nodes(email, nodes_data)
        if nodes_data.status_code > 300:
            print("create node error", title01, nodes_data.status_code, nodes_data.text)
            continue
        else:
            node_id = data_object.get_json_id(nodes_data.text)


        #create file
        if node_id is not None:
            file_name = 'test_preprints.pdf'
            file_reading = create_file.read_pdf(file_name)
            file_data = create_preprints.request_newfile(email, node_id, file_name, file_reading)
            if file_data.status_code > 300:
                print("create file error", author_main, file_data.status_code, file_data.text)
                continue
            else:
                file_id = data_object.get_files_id(file_data.text)

        if file_id is not None:
            preprints_data = fm.create_preprints(node_id, file_id)
            create_result = create_preprints.request_preprints(email, preprints_data)
            if create_result.status_code > 300:
                print("error: ", author_main, create_result.status_code, create_result.text)
                continue
            else:
                preprints_id = data_object.get_json_id(create_result.text)
                # contributor_data = fm.create_contributor(user_id)
                # r = create_contributor.patch_contributors(email, node_id, contributor_data)
                # if r.status_code > 300:
                #     print("not registed cotributor", email, r.status_code, r.text, preprints_id, user_id)

        if preprints_id is not None:
            p_year_month = kci_util.change_time(p_year_month).isoformat()
            #get subject
            subject = gs.get_subject(po)
            category_data = fm.create_preprints_patch_category(node_id, subject)
            r = create_preprints.patch_preprints(email, preprints_id, category_data)
            if r.status_code < 300:
                patch_data = fm.create_preprints_patch(preprints_id, p_year_month, po, abstract, doi)
                r = create_preprints.patch_preprints(email, preprints_id, patch_data)
                if r.status_code > 300:
                    print("patch error", r.status_code, r.text, preprints_id)
                    continue

        #add author_sub as contributors
            if author_sub is not None:
                result = author_sub.split(";")
                for name in result:
                    author_sub_data = create_preprints.request_user(author.get(name))
                    author_sub_id = data_object.get_json_id(author_sub_data.text)
                    if author_sub_id is not None:
                        sub_contributor_data = fm.create_contributor(author_sub_id)
                        r = create_preprints.patch_contributors(email, node_id, sub_contributor_data)
                        if r.status_code > 300:
                            print("add author_sub failed ", name, author_sub_id, preprints_id)

        #publish preprints to public
        if file_id is not None and preprints_id is not None:
            publish_data = fm.create_published(preprints_id)
            r = create_preprints.patch_preprints(email, preprints_id, publish_data)
            if r.status_code > 300:
                print('publish error ', r.status_code, r.text, title01, preprints_id)


    print("done! preprints")
    print("1 created in --- %s seconds ---" % (time.time() - start_time))
