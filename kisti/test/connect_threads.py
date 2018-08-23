import cx_Oracle
import threading
import json

pool = cx_Oracle.SessionPool('ks20', 'ks20+0913',
                             'b3d.kisti.re.kr:1251/KIS04', 2, 5, 1, threaded=True, encoding='UTF-8')


def theLongQuery():
    conn = pool.acquire()
    cursor = conn.cursor()
    cursor.arraysize = 25000
    print("TheLongQuery(): beginning execute...")
    cursor.execute("""
            select TITLE01, TITLE02, AUTHOR_MAIN, AUTHOR_SUB, 
            SJ_NM, ESJ_NM, VOLUME, ISSUE, P_YEAR_MONTH,
            PO, ABSTRACT, URL, DOI
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
            data['title01'] = row[0]
            data['title02'] = row[1]
            data['author_main'] = row[2]
            data['author_sub'] = row[3]
            data['sj_nm'] = row[4]
            data['esj_nm'] = row[5]
            data['volume'] = row[6]
            data['issue'] = row[7]
            data['p_year_month'] = row[8]
            data['po'] = row[9]
            data['abstract'] = row[10]
            data['url'] = row[11]
            data['doi'] = row[12]
            paper_list.append(data)

    print("TheLongQuery(): all done!")

    with open('kci_paper.json', 'w', encoding='utf-8') as outfile:
        json.dump(paper_list, outfile)
    print("CREATE JSON : done!")


def doALock():
    conn = pool.acquire()
    cursor = conn.cursor()
    print("DoALock(): beginning execute...")
    cursor.callproc("dbms_lock.sleep", (5,))
    print("DoALock(): done execute...")


thread1 = threading.Thread(None, theLongQuery)
thread1.start()

thread2 = threading.Thread(None, doALock)
thread2.start()

thread1.join()
thread2.join()

print("All done!")