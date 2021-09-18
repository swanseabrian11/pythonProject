import requests
import lxml
import time
import parsel
import json

# with open('C:\\Users\\asus\\Desktop\\text.txt') as fp:

   headers = {'user-agent': 'my-app/0.0.1'}
   data={'recharge':36,'fee_id':'ireader_nonrenew_vip'}
   url = https://www.gushiciju.com/shiji/7

   res_list = requests.get(url, data=data, headers=header)
   html_list=res_list.content.decode(utf8))
   jsonshici = json.load(res.content.decode(utf8))
   selector_list = parsel.selector(res_list)

  #  循环取所有诗词链接中的post数据
  for pl in urlarray:
    # url = pl.strip()
    res_shangxi = requests.post(url, data=data, headers=header)
    jsonshici = json.load(res.content.decode(utf8))
      shangxi = jsonshic['data']

      # for i in jsonshici
    selector = parsel.selector(shangxi)