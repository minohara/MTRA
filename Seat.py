# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:03:39 2020

@author: tomon
"""

# coding: UTF-8
#import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# URL関連
top_url = "https://cinemacity.co.jp/"
url = "https://res.cinemacity.co.jp/TicketReserver/studio/program/2081/252392"
# ヘッドレスモードを設定
options = Options()
options.add_argument('--headless')
# Chromeを起動
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)
# 一度トップページに行きCookieを取得
driver.get(top_url)
driver.get_cookies()
driver.get(url)
# soupオブジェクトを作成
soup = BeautifulSoup(driver.page_source, "lxml")
# 予約済みリストを取得して表示
for seat in soup.find_all("div", class_="reserved"):
 print(seat)
# Chromeドライバーを終了
driver.close()