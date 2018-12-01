import requests
import re
from bs4 import BeautifulSoup
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(3, 4)]
photos = []
for url in urls:
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    print(soup)
    imgs = soup.select('article.photo-item > a > img')
    for img in imgs:
        photo = img.get('src')
        photos.append(photo)
path = 'D://images/'
for item in photos:
    data = requests.get(item, headers=headers)
    photo_name = re.findall('\d+\/(.*?)\?a', item)
    print(photo_name)
    if photo_name:
        fp = open(path + photo_name[0], 'wb')
        fp.write(data.content)
        fp.close()