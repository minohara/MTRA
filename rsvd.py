# -*- coding: utf-8 -*-
"""
List Reserved Seat in MTRA database
    by Minohara Labo. Takushoku Univ.  (2021)
"""
import MySQLdb

conn = MySQLdb.connect(
    user='mtra',
    passwd='ophljH8PZI',
    host='localhost',
    db='mtra',
    charset='utf8mb4')

try:
    cursor=conn.cursor()
    cursor.execute("select * from screen;")
    print("ID  Name")
    scrn_name = []
    for scrn in cursor.fetchall():
        scrn_name.append(scrn[1])
        print("%2d. %s" % scrn)
    scrn_id = int(input("Input a screen ID: "))
    cursor.close()
    cursor=conn.cursor()
    cursor.execute("""
      select screen_id,`row`,`column`,count(*)
      from reservation join seat on reservation.seat_id = seat.id
      where screen_id=%d group by seat_id
      order by count(*);
    """ % scrn_id)
    for seat in cursor.fetchall():
        print("\"%s\"\t%s%d\t%6d" % (scrn_name[seat[0]], seat[1], seat[2], seat[3]))
    cursor.close()
except MySQLdb.Error as e:
    print("MySQLdb.Error: ", e)
conn.close()
