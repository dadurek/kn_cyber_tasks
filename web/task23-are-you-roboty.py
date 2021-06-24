import requests
from bs4 import BeautifulSoup

url = 'http://tasks.ctfd.kncyber.pl:7022'

s = requests.Session()
s.cookies.set("PHPSESSID", "70df6bf61da4c7f5159e03ccc1a74182")

for i in range(1,120):
    r = s.get(url)
    print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    code = str(soup.find('img'))[27:-3]
    print(code)
    s.post(url,{'captcha' : code})
