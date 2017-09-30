import requests
from bs4 import BeautifulSoup
import time
import json

npage = ''
oldpage=''
def f1(b,j):
    b=b[:j] + '-' + b[j+1:]
    return b
def f2(b,j):
    b=b[:j] + '+' + b[j+1:]
    return b

def crawl(a):
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

    response = ajax_crawl(v)

    #the response contains commas when value > 1k. So we need to handle it and store it as string, or maybe parse and then covert to float.
    #as of now code works for shares whos values are less than 1000
    return float(response)
    # for i in range(0,l):
    #     if(a[i]==" "):
    #         l1.append(i)
    # l2=len(l1)
    # for i in range(0,l2):
    #     c=f1(a,l1[i])
    #     a=c
    # for i in range(0,l2):
    #     c=f1(a,l1[i])
    #     a=c
    # for i in range(0,l2):
    #     d=f2(a,l1[i])
    #     a=d
    # u="http://money.rediff.com/companies/%s/%f?srchword=%s.&snssrc=sugg" %(c,v,d)
    # page = requests.get(u, headers={'Connection':'close'}) 
    # global npage
    # global oldpage
    # npage = page.content
    # if(len(oldpage)==0):
    #     oldpage=npage
    # else:
    #     if(oldpage == npage):
    #         print 'same html'
    # soup = BeautifulSoup(page.content, "lxml")
    # q=soup.find_all('span',id='ltpid',class_='bold')
    # val= [float(row.text) for row in q]
    # print 'Crawl=', val
    # page.close()
    # return val

def ajax_crawl(id=13190108):
    u="http://money.rediff.com/money1/currentstatus.php?companycode="+ str(id)
    res = requests.get(u)
    #print res.content
    j= json.loads(res.content)
    return j["LastTradedPrice"]


# j is a json object. A sample value of j is given below, we can use it to access any value.
# The current price is store in lasttradedprice.. we can collect other stuff too from json.
# {"LastTradedPrice":"2,487.60","Volume":"9,770","PercentageDiff":"-0.10","FiftyTwoWeekHigh":"2,707.40",
# "FiftyTwoWeekLow":"2,054.70","LastTradedTime":"28 Sep,11:52:35","ChangePercent":"-0.10",
# "Change":"-2.55","MarketCap":"476,201.27","High":"2,511.05","Low":"2,471.20","PrevClose":"2,490.15",
# "BonusSplitStatus":"0","BonusSplitRatio":"0-0"}






