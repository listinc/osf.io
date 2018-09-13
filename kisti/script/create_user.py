from osf import users
import time


if __name__ == '__main__':
    start_time = time.time()
    # if you want to create some user, insert value 1, create bulk user insert 2
    val = 2
    if val == 1:
        #data
        data = {}
        data['박진호'] = 'jino.kor@listinc.kr'
        data['테스트'] = 'test@li-st.com'
        users.create_the_user_execute(data)

    else:
        users.bulk_create_user()

    print("user created in --- %s seconds ---" % (time.time() - start_time))
