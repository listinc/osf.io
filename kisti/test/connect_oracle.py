import cx_Oracle

ip = 'b3d.kisti.re.kr'
port = 1251
SID = 'KIS04'
# dsn_tns = cx_Oracle.makedsn(ip, port, SID)

db = cx_Oracle.connect('ks20', 'ks20+0913', 'b3d.kisti.re.kr:1251/KIS04')

print(db)
