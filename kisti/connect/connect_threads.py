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
            select CN, TITLE01, TITLE02, AUTHOR_MAIN, AUTHOR_SUB, 
            SJ_NM, ESJ_NM, VOLUME, ISSUE, STARTPAGE, LASTPAGE, P_YEAR_MONTH,
            PO, ISSN, EISSN, RSC_EN, ABSTRACT, URLFLAG, FREG_EN, KCI_ID,
            EURLFLAG, DOI, URL, LDT, EDT, IUD, DBT, DBT2, LANG
            from
                KS20_KCI 
            where PO='한국기록관리학회' OR PO='한국기록학회' OR PO='한국도서관·정보학회' 
            OR PO='한국문헌정보학회' OR PO='한국비블리아학회' OR PO='한국서지학회' 
            OR PO='한국어정보학회' OR PO='한국정보관리학회'
                """)
    print("TheLongQuery(): done execute...")
    paper_list = []
    while True:
        rows = cursor.fetchmany()
        if not rows:
            break
        for row in rows:
            data = {}
            data['CN'] = row[0]
            data['TITLE01'] = row[1]
            data['TITLE02'] = row[2]
            data['AUTHOR_MAIN'] = row[3]
            data['AUTHOR_SUB'] = row[4]
            data['SJ_NM'] = row[5]
            data['ESJ_NM'] = row[6]
            data['VOLUME'] = row[7]
            data['ISSUE'] = row[8]
            data['STARTPAGE'] = row[9]
            data['LASTPAGE'] = row[10]
            data['P_YEAR_MONTH'] = row[11]
            data['PO'] = row[12]
            data['ISSN'] = row[13]
            data['EISSN'] = row[14]
            data['RSC_EN'] = row[15]
            data['ABSTRACT'] = row[16]
            data['URLFLAG'] = row[17]
            data['FREG_EN'] = row[18]
            data['KCI_ID'] = row[19]
            data['EURLFLAG'] = row[20]
            data['DOI'] = row[21]
            data['URL'] = row[22]
            data['LDT'] = row[23]
            data['EDT'] = row[24]
            data['IUD'] = row[25]
            data['DBT'] = row[26]
            data['DBT2'] = row[27]
            data['LANG'] = row[28]
            paper_list.append(data)

    print("TheLongQuery(): all done!")

    with open('kci_paper_library.json', 'w', encoding='utf-8') as outfile:
        json.dump(paper_list, outfile, cls=DateTimeEncoder)
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