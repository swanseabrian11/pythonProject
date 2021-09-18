import re

old_headers ='''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: xf_user=154223%2Cm4MUtlP1kINRM5LszQb3UNFPO3kmEy0Hw_2jUKiX; xf_csrf=-TgrMSK02A5UZtFn; Hm_lvt_ca31f7907f57f4d849f094509fb9bce3=1614301308,1614414069,1614493060,1614559041; xf_session=k9eDiRgIvjQGBSJtqTZ0IIgqnq1IfWZk; Hm_lpvt_ca31f7907f57f4d849f094509fb9bce3=1614574322
Host: www.hxzylt.com
If-Modified-Since: Mon, 01 Mar 2021 00:57:09 GMT
If-None-Match: "1560904394"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
'''

pattern = '^(.*?):[\s]*(.*?)$'
headers = ""
for line in old_headers.splitlines():
    headers += (re.sub(pattern,'\'\\1\': \'\\2\',',line)) + '\n'
print(headers[:-2])