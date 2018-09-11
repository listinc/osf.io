from osf import users
import time


if __name__ == '__main__':
    start_time = time.time()
    # if you want to create some user, insert value 1, create bulk user insert 2
    val = 1
    if val == 1:
        #data
        data = {}
        data['박진호'] = 'jino.kor@li-st.com'
        data['현미환'] = 'mhhyun@kisti.re.kr'
        users.create_the_user_execute(data)

    else:
        users.bulk_create_user()

    print("user created in --- %s seconds ---" % (time.time() - start_time))
