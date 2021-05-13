"""
List Reserved Seat in MTRA database
    by Minohara Labo. Takushoku Univ.  (2021)
"""
import MySQLdb
import csv

conn = MySQLdb.connect(
  user='mtra',
  passwd='ophljH8PZI',
  host='localhost',
  db='mtra',
  charset='utf8')

try:
    cursor=conn.cursor()
    cursor.execute("select * from screen;")
    print("ID  Name")
    for scrn in cursor.fetchall():
        print("%2d. %s" % scrn)
    scrn_id = int(input(">>> Select a screen: "))-1
    cursor.close()
    cursor=conn.cursor()
    cursor.execute("""
        select title, movie_id from screening join movie on screening.movie_id = movie.id
        where screen_id=%d group by movie_id
    """ % scrn_id)
    print("ID  Title")
    movies = []
    for i, movie in enumerate(cursor.fetchall()):
        movies.append(movie)
        print("%2d. %s" % (i+1, movie[0]) )
    cursor.close()
    id = int(input(">>> Select a movie: "))-1
    movie_id = movies[id][1]
    title = movies[id][0]
    print(title)
    cursor=conn.cursor()
    cursor.execute("""
        select id, start_time from screening where movie_id=%d and screen_id=%d
    """ % (movie_id, scrn_id))
    screenings = []
    for i, screening in enumerate(cursor.fetchall()):
        screenings.append(screening)
        print("%2d. %s" % (i+1, screening[1]) )
    cursor.close()
    id = int(input(">>> Select a Start time: "))-1
    print(title, screenings[id][1])
    cursor=conn.cursor()
    cursor.execute("""
        select time, sample_id from reservation join sample
        on reservation.sample_id = sample.id where screening_id=%d group by sample_id
    """ % screenings[id][0])
    samples = []
    for rsv in cursor.fetchall():
        delta=int((screenings[id][1] - rsv[0]).total_seconds()/60)
        samples.append((delta, rsv[1]))
    cursor.close()
    with open("movie--%d-%d.csv"%(movie_id,id), "w") as f:
        f.write("# %s %s\n" % (title, screenings[id][1]))
        writer = csv.writer(f)
        for sample in samples:
            cursor=conn.cursor()
            cursor.execute("""
                select `row`,`column` from reservation join seat
                on reservation.seat_id = seat.id where sample_id=%d and screening_id=%d
            """ % (sample[1], screenings[id][0]))
            seats = [sample[0]]
            for seat in cursor.fetchall():
                seats.append( seat[0]+str(seat[1]) )
            print(seats)
            writer.writerow(seats)
            cursor.close()
    f.close()
except MySQLdb.Error as e:
    print("MySQLdb.Error: ", e)
conn.close()
