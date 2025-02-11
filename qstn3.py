import requests as rq
import time

def url_check_Kar(url):
    try:
        res = rq.get(url,timeout=5)
        statusCode = res.status_code
        
        if(400 <= statusCode < 500):
            print("4xx error encountered for URL: " + url)
        elif(500 <= statusCode < 600):
            print("5xx error encountered for URL: " + url)
        else:
            print("The website is UP and running")
    except rq.exceptions.RequestException as e:
        print(e.response)
        return statusCode
        
        
url = input("URL Input : ")
url_check_Kar(url);

tout = 2;
while(True):
    stat = url_check_Kar(url);
    time.sleep(tout)
    
    if(stat != 200):
        tout *= 2