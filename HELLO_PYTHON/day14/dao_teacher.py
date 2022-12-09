import psycopg2
from psycopg2 import extras

class DaoTeacher:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
    def __del__(self):
        self.cur.close()
        self.connection.close()
        
    def selects(self):
        sql=f'''
            SELECT t_id,t_name,mobile,addr FROM teacher
            order by t_id
            '''
        result = []
        try :
            self.cur.execute(sql)
            data = self.cur.fetchall()
            for row in data:
                result.append(dict(row))
        except Exception as e:
            print(e)
        return result
    
    def select(self, t_id):
        sql=f'''
            SELECT t_id,t_name,mobile,addr FROM teacher
            where t_id = '{t_id}'
            '''
        try :
            self.cur.execute(sql)
            data = self.cur.fetchall()
        except Exception as e:
            print(e)
        # print(data, len(data), type(data))
        return dict(data[0])
    
    def insert(self, t_name,mobile,addr):
        sql=f'''
            insert into teacher
            values (nextval('t_seq'),'{t_name}','{mobile}','{addr}')
            '''
        # try :
        #     self.cur.execute(sql)
        # except Exception as e:
        #     print(e)
        #     return 0
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def update(self, t_id,t_name,mobile,addr):
        sql = f'''
            update    teacher
            set     t_name = '{t_name}',
                    mobile = '{mobile}',
                    addr = '{addr}'
            where     t_id = '{t_id}'
            '''
        # try :
        #     self.cur.execute(sql)
        # except Exception as e:
        #     print(e)
        #     return 0
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 
    
    def delete(self, t_id):
        sql = f'''
            delete from    teacher
            where     t_id = '{t_id}'
            '''
        # try :
        #     self.cur.execute(sql)
        # except Exception as e:
        #     print(e.args)
        #     return 0
        self.cur.execute(sql)
        self.connection.commit()
        return self.cur.rowcount 