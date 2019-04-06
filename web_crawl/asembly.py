from bs4 import BeautifulSoup

import urllib.request as url

url_domain = 'http://likms.assembly.go.kr'

#url_sub = '/bill/billDetail.do?'
url_sub = '/record/mhs-20-010.do'
#url_qstr = 'billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7'

url_str = url_domain+url_sub
#url_str = url_domain+url_sub+url_qstr
html = url.urlopen(url_str).read()

soup = BeautifulSoup(html, 'html.parser')

txt = soup.find(attrs="title4 liststyle").text#f12한후 class=title4 liststyle임,class뒤 부분을 찾아서 복사하면 됨

print(txt)