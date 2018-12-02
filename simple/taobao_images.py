from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import urllib.request

# 打开火狐
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)
# 这里关键字可以自己修改
KEYWORD = '男装'


#定义一个获取索引页信息的函数
def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

# 解析获取到的索引页的信息，将商品的信息从中提取出来
def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    photos = []
    for item in items:
        photos.append(item.find('.pic .img').attr('data-src'))
        # 其他数据，可以爬取下来放到数据库
        # product= {
        #     'image': item.find('.pic .img').attr('data-src'),
        #     'price': item.find('.price').text(),
        #     'deal': item.find('.deal-cnt').text(),
        #     'title': item.find('.title').text(),
        #     'shop': item.find('.shop').text(),
        #     'location': item.find('.location').text()
        # }
        # print(product)

    for item in photos:
        item = "https:"+item
        start = item.rfind("/")
        end = item.rfind("_!!")
        print(item)
        with urllib.request.urlopen(item, timeout=30) as response, open("D://images/%s.jpg" % (item[start:end]), 'wb') as f_save:
            f_save.write(response.read())
            f_save.flush()
            f_save.close()

# 设置页码
MAX_PAGE = 1
#实现页码的遍历
if __name__ == '__main__':
    for i in range(1, MAX_PAGE+1):
        index_page(i)
 
 
 
 
 
 
 
 
 