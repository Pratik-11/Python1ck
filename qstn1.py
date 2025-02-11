ip = input("Enter Ip : ")
ipparts = ip.split(".")
if(len(ipparts) != 4):
    print("NO not in ipv4")
else:
    a, b, c, d = map(int, ipparts)
if(a==10):
    print("Private ip")
elif( a == 172 and 16 <= b <=31):
    print("Private ip")
elif(a == 192 and b == 168):
    print("Private ip")
else:
    print("Public ip")
for i in range(0,4):
    if(0 <= int(ipparts[i]) <=255):
        if(i == 3):
            print("Yes it is ipv4")
    else:
        print("NO not in ipv4")
        break
