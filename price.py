import requests
import time
import json


def crawl(a):
    
    l=len(a)
    c=a
    d=a
    l1=[]
    v=0
    if(a=="Tata Consultancy Services Ltd"):
        v=13020033
    elif(a=="Mahindra Mahindra Financial Services Ltd"):
        v=10520003.14
    elif(a=="Kotak Mahindra Bank Ltd"):
        v=14060005
    elif(a=="Indian Oil Corporation Ltd"):
        v=12140022
    elif(a=="Larsen Toubro Infotech Ltd"):
        v=13190108
    elif(a=="Ashok Leyland Ltd"):
        v=10510001
    elif(a=="DFHL"):
        v=14080006
    elif(a=="sterlite"):
        v=15140056

    response = ajax_crawl(v)
    print (response)
    return response
    

def ajax_crawl(id):
    u="http://money.rediff.com/money1/currentstatus.php?companycode="+ str(id)
    res = requests.get(u)
    #print res.content
    j= json.loads(res.content)
    return j["LastTradedPrice"]






