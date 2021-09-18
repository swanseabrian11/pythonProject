# coding=utf8
import requests
import lxml
import time
import parsel
import json
import pandas
import urllib
from bs4 import BeautifulSoup
import time
import re
import chardet

# with open('C:\\Users\\asus\\Desktop\\text.txt') as fp:
# 确定请求地址URL地址


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'xf_user=154223%2Cm4MUtlP1kINRM5LszQb3UNFPO3kmEy0Hw_2jUKiX; xf_csrf=euaiRH4eytVyXoME; Hm_lvt_ca31f7907f57f4d849f094509fb9bce3=1614128102,1614301308,1614414069; xf_session=IqGPZAz36tWMlL4T7v5Mz-fjntQHLd8y; Hm_lpvt_ca31f7907f57f4d849f094509fb9bce3=1614417780',
    'Host': 'www.hxzylt.com',
    'If-Modified-Since': '',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
headers1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'xf_user=154223%2Cm4MUtlP1kINRM5LszQb3UNFPO3kmEy0Hw_2jUKiX; xf_csrf=-TgrMSK02A5UZtFn; Hm_lvt_ca31f7907f57f4d849f094509fb9bce3=1614301308,1614414069,1614493060,1614559041; xf_session=k9eDiRgIvjQGBSJtqTZ0IIgqnq1IfWZk; Hm_lpvt_ca31f7907f57f4d849f094509fb9bce3=1614574322',
'Host': 'www.hxzylt.com',
'If-Modified-Since': '',
'If-None-Match': '',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "http://www.hxzylt.com/forums/390/"
url1 = "http://www.hxzylt.com/attachments/94193/"
# 得到附件的headers信息
r=requests.get(url1,headers =headers1,allow_redirects=False)
# print(chu.encoding)

s = r.status_code
print (s)
# r.headers.encoding= "utf-8"
# rr = r.headers
# rd =rr.
chu = r.headers['Content-Disposition']
# ss = chu.encode('ISO-8859-1')
# print (r.headers)
# chu1 = chu.encode('gbk').decode()
# chu1 = chu.encode()
# aa = chardet.detect(chu1)
# chu.encoding = "utf-8"
chu1 = chu.encode('ISO-8859-1').decode()
s1 = chu1.split(";")
s = re.search(r'"([^."]+).([^."]+)"',s1[1])
print(s.group(2))

res_list = requests.get(url, headers=headers)
html_list = res_list.content.decode(utf8))
res_list.encoding = "utf-8"
soup = BeautifulSoup(res_list.text, "html.parser")

soup1 = soup.prettify()
data1 = []
post_items = soup.find_all("div", attrs={"class":"structItem-title"})
# print(type(post_items))
for post_item in post_items:
     link=post_item.find("a", attrs={"href":re.compile(r".threads/\d+")})
     # print (link["href"])
     # print('-----'*30)
     data1.clear()
     # data1.append("http://www.hxzylt.com%s"%link["href"])
     data1.append("http://www.hxzylt.com" +link["href"])
     # print(data1)

     for data in data1:
         data_url = requests.get(data, headers=headers)
         # html_list = res_list.content.decode(utf8))
         res_list.encoding = "utf-8"
         soup1 = BeautifulSoup(data_url.text, "html.parser")
         data_url1 = soup1.find("a", attrs={"href":re.compile(r"./attachments/\d+")})
def download_file(fname,furl)
    r = requests.get(furl)
    with open(path, "wb") as f:
        f.write(r.content)
    f.close()
