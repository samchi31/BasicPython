import psycopg2;

connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

# connection.autocommit = True
cur = connection.cursor()

col01 = '4'
col02 = '8'
col03 = '8'

# sql = '''
#         update    sample
#         set     col02 = '{}',
#                 col03 = '{}'
#         where     col01 = '{}'
#       '''.format(col02, col03, col01)
      
sql = f'''
        update    sample
        set     col02 = '{col02}',
                col03 = '{col03}'
        where     col01 = '{col01}'
      '''

cur.execute(sql)

rowcount = cur.rowcount 
print(rowcount)

connection.commit()


cur.close()
connection.close()