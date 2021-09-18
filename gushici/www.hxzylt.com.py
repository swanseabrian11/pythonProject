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
#添加头文件
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'xf_user=154223%2Cm4MUtlP1kINRM5LszQb3UNFPO3kmEy0Hw_2jUKiX; xf_csrf=Fct9g0LmUh68PYR6; xf_session=xyEo3sVYZ9yr902dcK-pLwa2HszwqZqV; Hm_lvt_ca31f7907f57f4d849f094509fb9bce3=1614128102,1614301308; Hm_lpvt_ca31f7907f57f4d849f094509fb9bce3=1614301308',
    'Host': 'www.hxzylt.com',
    'If-Modified-Since': 'Fri, 26 Feb 2021 01:01:43 GMT',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# with open('C:\\Users\\asus\\Desktop\\text.txt') as fp:
# 确定请求地址URL地址
def get_index(page)：
# url拼接
url = f'http://www.hxzylt.com/forums/390/page-{page}'

response = requests.get(url, headers=header)
try:
    if response.status_code == 200:
    return response.text
else:
return None
except RequestException:
return None
# html_list = res_list.content.decode(utf8))
res_list.encoding = "utf-8"


def parse_index(html)：


data = []

soup = beautifulsoup(response.text, "html.parser")

# post_items = soup.findall("a", attrs={"class": "structItem-title"})
post_items = soup.find_all("div", attrs={"class":"structItem-title"})
# print(type(post_items))
for post_item in post_items:
     link=post_item.find("a", attrs={"href":re.compile(r".threads/\d+")})
     # print (link["href"])
     # print('-----'*30)
     data.clear()
     # data1.append("http://www.hxzylt.com%s"%link["href"])
     data.append("http://www.hxzylt.com" +link["href"])
     # print(data1)

# for post_item in post_items:
#         data.append(“http: // www.hxzylt.com % s” % post_item["href"])
#         pass
#获取详情页
def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

#获取详情页中的下载地址
def parse_detail(html):
    response = requests.get(url1, headers=headers1, allow_redirects=False)
    # print(chu.encoding)
    #打印HTTP返回值 是200还是304
    s = r.status_code
    print(s)
    # r.headers.encoding= "utf-8"
    # rr = r.headers
    # rd =rr.
    # 取headers中的信息
    chu = r.headers['Content-Disposition']
    # ss = chu.encode('ISO-8859-1')
    # print (r.headers)
    # chu1 = chu.encode('gbk').decode()
    # chu1 = chu.encode()
    # aa = chardet.detect(chu1)
    # chu.encoding = "utf-8"
    对Headers中的信息进行转码
    chu1 = chu.encode('ISO-8859-1').decode()
    s1 = chu1.split(";")
    s = re.search(r'"([^."]+).([^."]+)"', s1[1])
    print(s.group(2))
def save_to_folder(result):
        dw_url = requests.get(url=url1, headers=headers1, allow_redirects=False, verify=False, stream=True)
        with open('%s.%s' % (dname, dhouzhui), 'wb') as fd:
            # 此处断点 可查看 文件名: res.headers['Content-Disposition'].encode('latin1').decode()
            # print(res.headers['Content-Disposition'].encode('latin1').decode())
            # print('下载新的……')
            for chunk in dw_url.iter_content(chunk_size=1024):
                if chunk:
                    fd.write(chunk)
def main():
  for page in range(1, 247):
    html = get_index(page)
    if html:
      article_urls = parse_index(html)
      for article_url in article_urls:
        article_html = get_detail(article_url)
        if article_html:
          result = parse_detail(article_html)
          def save_to_folder(result)
def if __name__ == '__main__':
