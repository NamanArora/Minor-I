import requests
import time
import json
from news import head


def code(a):
    
    l=len(a)
    c=a
    d=a
    l1=[]
    v=0
    
    if(a=="Mahindra Mahindra Financial Services Ltd"):
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

    ajax_crawl(v)
    nws(a,v)
    
    

def ajax_crawl(id):
    u="http://money.rediff.com/money1/currentstatus.php?companycode="+ str(id)
    res = requests.get(u)
    j= json.loads(res.content)
    print "Price = " + j["LastTradedPrice"]
    print "Volume = " +j["Volume"]
    print "Yearly Highest Price = " +j["FiftyTwoWeekHigh"]
    print "Yearly Lowest Price = " +j["FiftyTwoWeekLow"]
    print "Highest Price of the Day = " +j["High"]
    print "Lowest Price of the Day = " +j["Low"]
    print "Previous Close = " +j["PrevClose"]

    
def nws(sharename,v):
    print"   "
    print "HEADLINES RELATED TO THE SHARE: "
    print "  "
    head(sharename,v)
    





