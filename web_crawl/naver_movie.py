
from selenium import webdriver      # imports

from time import sleep

from bs4 import BeautifulSoup

ctx = 'C:/Users/ezen/PycharmProjects/'
driver = webdriver.Chrome(ctx+"chromedriver")

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

soup = BeautifulSoup(driver.page_source,'html.parser')#lxml가 에러 나면 parser로 변경

print(soup.prettify())

all_divs = soup.find_all('div',attrs={'class':'tit3'})

products = [div.a.string for div in all_divs]  #수정됨

for i in products:

    print(i)

driver.close()



