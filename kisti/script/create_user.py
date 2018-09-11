from osf import bulk_create_user
import time


if __name__ == '__main__':
    start_time = time.time()
    #data
    data = {}
    data['박진호'] = 'jino.kor@li-st.com'
    data['현미환'] = 'mhhyun@kisti.re.kr'
    bulk_create_user.create_the_user_execute(data)
    print("user created in --- %s seconds ---" % (time.time() - start_time))
