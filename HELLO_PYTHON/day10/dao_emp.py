import psycopg2
from psycopg2 import extras

class DaoSample:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
    def __del__(self):
        self.cur.close()
        self.connection.close()
        
    def selects(self):
        sql=f'''
            SELECT e_id,e_name,sex,addr FROM emp
            '''
        result = []
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            result.append(dict(row))
        return result
    
    def select(self, e_id):
        sql=f'''
            SELECT e_id,e_name,sex,addr FROM emp
            where e_id = {e_id}
            '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        # print(data, len(data), type(data))
        return dict(data[0])
    
    def insert(self, e_id,e_name,sex,addr):
        sql=f'''
            insert into emp
            values ('{e_id}','{e_name}','{sex}','{addr}')
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def update(self, e_id,e_name,sex,addr):
        sql = f'''
            update    emp
            set     e_name = '{e_name}',
                    sex = '{sex}',
                    addr = '{addr}'
            where     e_id = '{e_id}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def delete(self, e_id):
        sql = f'''
            delete from    emp
            where     e_id = '{e_id}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 