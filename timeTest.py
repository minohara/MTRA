# -*- coding: utf-8 -*-

from datetime import datetime
import MySQLdb

now = datetime.now()

conn = MySQLdb.connect(
 user='mtra',
 passwd='ophljH8PZI',
 host='localhost',
 db='sample_db',
 charset='utf8')

cursor=conn.cursor()

try:
    # CREATE
    # id, name だけのシンプルなテーブルを作成。id を主キーに設定。
#    cursor.execute("DROP TABLE IF EXISTS `timestamp`")
    cursor.execute("""CREATE TABLE IF NOT EXISTS `timestamp` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `time` DATETIME NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

    cursor.execute("INSERT INTO timestamp(time) VALUES ('%s')" % now.isoformat())
    print(cursor.lastrowid)

except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)

conn.commit()
conn.close()
