from osf import confirm
import time


if __name__ == '__main__':
    start_time = time.time()
    confirm.confirm_user()
    print("--- %s seconds ---" % (time.time() - start_time))
