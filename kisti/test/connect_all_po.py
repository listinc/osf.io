import cx_Oracle
import threading
import json
from datetime import datetime


pool = cx_Oracle.SessionPool('ks20', 'ks20+0913',
                             'b3d.kisti.re.kr:1251/KIS04', 2, 5, 1, threaded=True, encoding='UTF-8')


def theLongQuery():
    conn = pool.acquire()
    cursor = conn.cursor()
    cursor.arraysize = 25000
    print("TheLongQuery(): beginning execute...")
    cursor.execute("""
            select 
            PO
            from
                KS20_KCI 
            where TO_NUMBER(P_YEAR_MONTH) > 201607
                """)
    print("TheLongQuery(): done execute...")
    paper_list = []
    while True:
        rows = cursor.fetchmany()
        if not rows:
            break
        for row in rows:
            paper_list.append(row[0])

    print("TheLongQuery(): all done!")

    paper_po = list(set(paper_list))
    with open('kci_paper_po.json', 'w', encoding='utf-8') as outfile:
        json.dump(paper_po, outfile, cls=DateTimeEncoder)
    print("CREATE JSON : done!")


def doALock():
    conn = pool.acquire()
    cursor = conn.cursor()
    print("DoALock(): beginning execute...")
    cursor.callproc("dbms_lock.sleep", (5,))
    print("DoALock(): done execute...")


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


if __name__ == "__main__":
    thread1 = threading.Thread(None, theLongQuery)
    thread1.start()

    thread2 = threading.Thread(None, doALock)
    thread2.start()

    thread1.join()
    thread2.join()

    print("All done!")