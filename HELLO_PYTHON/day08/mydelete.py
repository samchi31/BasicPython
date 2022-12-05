import psycopg2;

connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

# connection.autocommit = True
cur = connection.cursor()

col01 = '4'
      
sql = f'''
        delete from    sample
        where     col01 = '{col01}'
      '''

cur.execute(sql)

rowcount = cur.rowcount 
print(rowcount)

connection.commit()


cur.close()
connection.close()