import psycopg2;

connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

# connection.autocommit = True
cur = connection.cursor()

sql = '''
        insert into sample 
        values ('4','4','4')
      '''

cur.execute(sql)

rowcount = cur.rowcount 
print(rowcount)

connection.commit()


cur.close()
connection.close()