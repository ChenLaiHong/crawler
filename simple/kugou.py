import requests
import time
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
    host="localhost",       # 数据库主机地址
    user="root",    # 数据库用户名
    passwd="123456",   # 数据库密码
    database="test"  # 先自己手动创建数据库
)
mycursor = mydb.cursor()

# 数据表只能创建一次
# mycursor.execute("CREATE TABLE kugou (id INT AUTO_INCREMENT PRIMARY KEY, rank VARCHAR(255), singer VARCHAR(255), song VARCHAR(255), time VARCHAR(255))")
sql = "INSERT INTO kugou (rank, singer, song, time) VALUES (%s, %s, %s, %s)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    ranks = soup.select(".pc_temp_num")
    titles = soup.select(".pc_temp_songlist > ul > li > a")
    songs_times = soup.select(".pc_temp_time")

    for rank, title, song_time in zip(ranks, titles, songs_times):
        data = (rank.get_text().strip(),title.get_text().split('-')[0].strip(),title.get_text().split('-')[1].strip(),song_time.get_text().strip())
        print(data)
        print("---------------------------------")
        mycursor.execute(sql, data)
        mydb.commit()

if __name__ == "__main__":
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        get_info(url)
        time.sleep(1)
