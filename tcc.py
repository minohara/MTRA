# -*- coding: utf-8 -*-
"""
Scrape Reservation Data from Tachikawa Cinemacity
    by Minohara Labo. Takushoku Univ.  (2021)
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import MySQLdb
from parse import parse
from datetime import datetime

# 上映時間の文字列を datetime の tuple に変換
def parseTime(time):
    p = parse("{:d}年{:d}月{:d}日({}) {:d}:{:d}({:d}:{:d})",time)
    start = datetime(p[0],p[1],p[2],p[4],p[5])
    end = datetime(p[0],p[1],p[2],p[6],p[7])
    return (start, end)

# 上映回(rtb)のデータ処理
def procRtb(rtb):
    if (rtb != None):
        for rtbLi in rtb.find_all("li"):
            rtbAnchor = rtbLi.find("a")
            rtbUrl = topUrl+rtbAnchor["href"]
            driver.get(rtbUrl)
            rtbPage = BeautifulSoup(driver.page_source, "lxml")
            time = rtbPage.find("div", id="selected-time").string.strip()
            screenTime = parseTime(time)
            studio = rtbPage.find("span", class_="studio-name").string
            cursor=conn.cursor()
            cursor.execute("SELECT id FROM `screen` WHERE `name`='%s'" % studio)
            screen_id = cursor.fetchone()[0]
            cursor.close()
            cursor=conn.cursor()
            cursor.execute("""INSERT IGNORE INTO `screening`(
            `movie_id`, `screen_id`, `start_time`, `end_time`, `url`)
            VALUES ( %d, %d, '%s', '%s', '%s')"""\
            % (movie_id, screen_id, screenTime[0].isoformat(),\
            screenTime[1].isoformat(), rtbUrl))
            cursor.close()
            rsvdSeat = []
            for seat in rtbPage.find_all("div", class_="unclickable"):
                seatName = seat.get('id')
                seatRow = seatName[0]
                seatColumn = int(seatName[1:])
                cursor=conn.cursor()
                cursor.execute("""INSERT INTO `reservation` (
                `screening_id`, `seat_id`, `sample_id`)
                VALUES (
                (SELECT id FROM `screening` WHERE
                `movie_id`=%d AND `screen_id`=%d AND `start_time`='%s'),
                (SELECT id FROM `seat` WHERE
                `screen_id`=%d AND `row`='%s' AND `column`=%d),
                %d )""" \
                % (movie_id, screen_id, screenTime[0].isoformat(),\
                screen_id, seatRow, seatColumn, sample_id))
                rsvdSeat.append(seatName)
                cursor.close()
            print("%s %s %s" % (time, studio, rsvdSeat))

# データベース接続
conn = MySQLdb.connect(
 user='mtra',
 passwd='ophljH8PZI',
 host='localhost',
 db='mtra',
 charset='utf8mb4')

# webページの設定
topUrl = "https://res.cinemacity.co.jp"
showingUrl = topUrl + "/TicketReserver/showing"
options = Options()
options.add_argument('--headless')
# webdriverを起動
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=options)
try:
    # データ取得時刻をデータベースに登録
    now = datetime.now()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO `sample`(`time`) VALUES ('%s')"\
    % now.isoformat())
    sample_id = cursor.lastrowid
    cursor.close()
    # 上映中ページを取得
    driver.get(showingUrl)
    soup = BeautifulSoup(driver.page_source, "lxml")
    showing = soup.find("div", id="showing")
    # 上映中の各映画について
    for anchor in showing.find_all("a"):
        driver.get(topUrl+anchor["href"])
        movie = BeautifulSoup(driver.page_source, "lxml")
        # 映画情報(タイトル)をデータベースに登録
        title = movie.find("span", class_="movie-title").string
        print(title)
        cursor=conn.cursor()
        cursor.execute("""INSERT IGNORE INTO `movie`(`title`)
        VALUES ('%s');""" % title)
        cursor.close()
        # 映画情報のID取り出し
        cursor=conn.cursor()
        cursor.execute("SELECT `id` FROM `movie` WHERE `title`='%s'" % title)
        movie_id = cursor.fetchone()[0]
        cursor.close()
        # 当日(各映画トップページ内)の上映時間の処理
        procRtb(movie.find("div", id="rtb"))
        # 翌日以降の上映(rdb)の処理
        rdb = movie.find("div", id="rdb")
        if (rdb != None):
            for rdbAnchor in rdb.find_all("a"):
                driver.get(topUrl+rdbAnchor["href"])
                rdbPage = BeautifulSoup(driver.page_source, "lxml")
                procRtb(rdbPage.find("div", id="rtb"))
except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)
conn.commit()
conn.close()
# webdriverを終了
driver.close()
