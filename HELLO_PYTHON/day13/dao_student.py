import psycopg2
from psycopg2 import extras

class DaoStudent:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
    def __del__(self):
        self.cur.close()
        self.connection.close()
        
    def selects(self):
        sql=f'''
            SELECT s_id,s_name,mobile,address FROM student
            order by s_id
            '''
        result = []
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            result.append(dict(row))
        return result
    
    def select(self, s_id):
        sql=f'''
            SELECT s_id,s_name,mobile,address FROM student
            where s_id = '{s_id}'
            '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        # print(data, len(data), type(data))
        return dict(data[0])
    
    def insert(self, s_id,s_name,mobile,address):
        sql=f'''
            insert into student
            values ('{s_id}','{s_name}','{mobile}','{address}')
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def update(self, s_id,s_name,mobile,address):
        sql = f'''
            update    student
            set     s_name = '{s_name}',
                    mobile = '{mobile}',
                    address = '{address}'
            where     s_id = '{s_id}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def delete(self, s_id):
        sql = f'''
            delete from    student
            where     s_id = '{s_id}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 