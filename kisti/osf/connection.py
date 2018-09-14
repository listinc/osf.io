import psycopg2.extras


class OSFDB():
    def __init__(self):
        self.host = 'localhost'
        self.db_name = 'osf'
        self.user = 'postgres'
        self.conn_string = "host='{}' dbname='{}' user='{}'".format(self.host, self.db_name, self.user)
        self.conn = psycopg2.connect(self.conn_string)

    def connect(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cursor

    def close(self, curs):
        curs.close()
        self.conn.close()
