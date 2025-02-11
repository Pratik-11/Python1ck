import re

def if_gmail(str):
    pattern = r"^[a-z0-9_-]+$"
    return bool(re.match(pattern,str));


email = input("Enter a Gmail : ")
email = email.lower()
twostuff = email.split("@")

while(True):
    if('@' not in email):
        print("Not a valid Gmail no @")
        break
    if(twostuff[1] != "gmail.com"):
        print("Not a valid Gmail no gmail.com")
        break
    if(len(twostuff[0]) <6):
        print("Less than 6 charachters not allowed")
        break
    if(len(twostuff[0]) >30):
        print("More than 30 charachters not allowed")
        break
    if(if_gmail(twostuff[0])):
        print("Yes Valid Gmail");
    else:
        print("Not a Valid Gmail only a-z, 0-9, _ - allowed");
    break