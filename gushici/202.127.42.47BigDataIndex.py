import requests
import lxml
import time
import parsel
import json
import pandas
import urllib
import time

# with open('C:\\Users\\asus\\Desktop\\text.txt') as fp:
# 确定请求地址URL地址
def get_pagelist()
 # python时间戳
 nd = str(int(time.time()*1000))
 data = {'name': '',
'_search': 'false',
'nd': nd,
'rows': '20',
'page': '2',
'sidx': 'AppDate',
'sord': 'desc'}
 pass
for i range(100)

def get_json()
 url = "http://202.127.42.47:6009/Home/GetBigScreenlist"
 headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '74',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': '202.127.42.47:6009',
'Origin': 'http://202.127.42.47:6009',
'Referer': 'http://202.127.42.47:6009/Home/BigDataIndex',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
 headers1 = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': '202.127.42.47:6009',
'Referer': 'http://202.127.42.47:6009/Home/BigDataIndex',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
 data={
 '_search': 'false',
'nd': nd,
'rows': '20',
'page': '1',
'sidx': 'AppDate',
'sord': 'desc'}

 data1={
 'cropname': "item['TempName']",
 'type': '1'}

# 发送请求数据

 res_list_json = requests.post(url, data=data, headers=headers)
 res_list_json = res_list_json.content.decode("utf-8")
# print(res_list_json)

# 请求json网页列表数据
 json_data = json.loads(res_list_json)
# print(json_data)
 alljson =json_data["rows"]
# print(type(json_data))
# print(alljson)

# 请求json网页点击数据
def get_clickjsonurl()
# json_click_url_arg = json_data['rows']['TempName']
 for item in alljson:
 # 判断是否是中文
  if u'\u4e00' <=item['TempName'] <= u'\u9fff':
  # 如果是中文则转码
   tn = urllib.parse.quote(item['TempName'])
 # tnutf =tn.encode("gbk")
   json_click_url = f"http://202.127.42.47:6009/Home/PostCropDetail?cropname={tn}++++++++++++++++++++++++++++++++++++++++++++&type=1"
  else:
   tn = item['TempName']
   json_click_url = f"http://202.127.42.47:6009/Home/PostCropDetail?cropname={tn}++++++++++++++++++++++++++++++++++++++++++++&type=1"
def get_clickjsondata()
  res_list_json1 = requests.get(url = json_click_url, headers=headers1)
  res_list_json1 = res_list_json1.content.decode("utf-8")
  # 请求json网页列表数据
  json_data1 = json.loads(res_list_json1)
  print(json_data1)
  # print(res_list_json1)
  # print(res_list_json)
    # print(item['TempName'])
 # print(json_click_url )
# print(json_click_url_arg)
# json_click_url =
# 保存数据
def save_toexcel()
 df = pandas.DataFrame(alljson)
 df.to_excel("list1.xlsx")
# html_list = res_list_json.content.encode(utf8))
# jsonshici = json.load(res.content.decode(utf8))
# selector_list = parsel.selector(res_list)
#
#   #  循环取所有诗词链接中的post数据
#   for pl in urlarray:
#     # url = pl.strip()
#     res_shangxi = requests.post(url, data=data, headers=header)
#     jsonshici = json.load(res.content.decode(utf8))
#       shangxi = jsonshic['data']
#
#       # for i in jsonshici
#     selector = parsel.selector(shangxi)