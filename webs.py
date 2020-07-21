from selenium import webdriver
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

count = 0

driver = webdriver.Safari()

def img_download(url):
    global count
    driver.get(url)
    imgs = driver.find_elements_by_tag_name('img')
    srcs = list()

    for img in imgs:
        srcs.append(img.get_attribute('src'))

    for img in srcs:
        urllib.request.urlretrieve(img, "data/max"+str(count)+".png")
        count += 1

pages = ['https://multi.xnxx.com/category/hentai/p-'+str(i)+'/' for i in range(1,8)]

for page in pages:
    img_download(page)