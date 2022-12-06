import psycopg2, psycopg2.extras;

# connection = psycopg2.connect("host=192.168.0.1 dbname=postgres user=postgres password=1234 port=5432")
# 또는
connection = psycopg2.connect(host="localhost", dbname="python", user="postgres", password="python", port=5432)

cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("SELECT col01,col02,col03 FROM sample")

data = cur.fetchall()

print(data,type(data))

cur.close()
connection.close()