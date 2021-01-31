# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:27:54 2021

@author: tomon
"""

# MySQLdb をインポート
import MySQLdb
# datetime をインポート
from datetime import datetime
# selenum 関連のインポート
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# URL関連
top_url = "https://cinemacity.co.jp/"
url = "https://res.cinemacity.co.jp/TicketReserver/studio/program/2002/253306"
# ヘッドレスモードを設定
options = Options()
options.add_argument('--headless')
# Chromeを起動
#driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)
driver = webdriver.Chrome(options=options)
# 一度トップページに行きCookieを取得
driver.get(top_url)
driver.get_cookies()
driver.get(url)
# soupオブジェクトを作成
soup = BeautifulSoup(driver.page_source, "lxml")
ary = []
for seat in soup.find_all("div", class_="unclickable"):
    ary.append(seat.get('id'))

# 現在時刻を取得
now = datetime.now()

# データベース接続とカーソル生成
conn = MySQLdb.connect(
 user='mtra',
 passwd='ophljH8PZI',
 host='localhost',
 db='sample_db',
 charset='utf8')

cursor=conn.cursor()

# エラー処理（例外処理）
try:
    # CREATE
    # timestamp table の作成
    cursor.execute("""CREATE TABLE IF NOT EXISTS `timestamp` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `time` DATETIME NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")
    # sample table の作成
#    cursor.execute("DROP TABLE IF EXISTS `sample`")
    cursor.execute("""CREATE TABLE IF NOT EXISTS `sample` (
    `id` int NOT NULL AUTO_INCREMENT,
    `timestamp_id` int not null,
    `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
    PRIMARY KEY (id),
    foreign key (`timestamp_id`) references `timestamp`(`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

    # 時刻情報登録
    cursor.execute("INSERT INTO timestamp(time) VALUES ('%s')" % now.isoformat())
    ts_id = cursor.lastrowid
    # 座席情報登録
    for seat in ary:
        cursor.execute("INSERT INTO `sample`(`timestamp_id`, `name`) VALUES ('%d','%s');" % (ts_id, seat))

except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)

conn.commit()
conn.close()

# print(ary)
# Chromeドライバーを終了
driver.close()
