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
        result = []
        self.cur.execute("SELECT col01,col02,col03 FROM sample")
        data = self.cur.fetchall()
        for row in data:
            result.append(dict(row))
        return result
    
    def select(self, col01):
        self.cur.execute("SELECT col01,col02,col03 FROM sample where col01='{}'".format(col01))
        data = self.cur.fetchall()
        # print(data, len(data), type(data))
        return dict(data[0])
    
    def insert(self, col01,col02,col03):
        sql=f'''
            insert into sample
            values ('{col01}','{col02}','{col03}')
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def update(self, col01,col02,col03):
        sql = f'''
            update    sample
            set     col02 = '{col02}',
                    col03 = '{col03}'
            where     col01 = '{col01}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def delete(self, col01):
        sql = f'''
            delete from    sample
            where     col01 = '{col01}'
            '''
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
        
# if __name__ == '__main__':
#     ds = DaoSample()
#     list = ds.selects();
#     print(list)
#
#     data = ds.select("1")
#     print(data)
#
#     res1 = ds.insert(3, 3, 3)
#     print(res1)
#
#     res2 = ds.update(3, 6, 6)
#     print(res2)
#
#     res3 = ds.delete(3)
#     print(res3)