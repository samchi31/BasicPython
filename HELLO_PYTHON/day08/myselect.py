import psycopg2;

# connection = psycopg2.connect("host=192.168.0.1 dbname=postgres user=postgres password=1234 port=5432")
# 또는
connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

cur = connection.cursor()

cur.execute("SELECT col01,col02,col03 FROM sample")
# (id, num, data) = cur.fetchone()
# print(f"{id}, {num}, {data}")

data = cur.fetchall()
for item in data:
    print(item)

cur.close()
connection.close()