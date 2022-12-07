import psycopg2
from psycopg2 import extras

class DaoMember:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
    def __del__(self):
        self.cur.close()
        self.connection.close()
        
    def selects(self):
        sql=f'''
            SELECT m_id,m_nm,tel,ymd FROM member
            '''
        result = []
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            result.append(dict(row))
        return result
    
    def select(self, m_id):
        sql=f'''
            SELECT m_id,m_nm,tel,ymd FROM member
            where m_id = '{m_id}'
            '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        # print(data, len(data), type(data))
        return dict(data[0])
    
    def insert(self, m_id,m_nm,tel,ymd):
        sql=f'''
            insert into member
            values ('{m_id}','{m_nm}','{tel}','{ymd}')
            '''

        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def update(self, m_id,m_nm,tel,ymd):
        sql = f'''
            update    member
            set     m_nm = '{m_nm}',
                    tel = '{tel}',
                    ymd = '{ymd}'
            where     m_id = '{m_id}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def delete(self, m_id):
        sql = f'''
            delete from    member
            where     m_id = '{m_id}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 