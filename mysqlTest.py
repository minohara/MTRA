import MySQLdb

con = MySQLdb.connect(
  user='mtra',
  passwd='ophljH8PZI',
  host='localhost',
  db='mtra',
  charset='utf8'
)

cur = con.cursor()

sql = 'select name from screen'
cur.execute(sql)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
con.close()
