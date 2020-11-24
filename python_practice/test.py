import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
# print(response.read())

import requests
r = requests.get("http://www.baidu.com")
print(r)
print(r.status_code)
print(r.encoding)
print(r.text)