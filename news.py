from bs4 import BeautifulSoup
import requests



def f1(b,j):
    b=b[:j] + '-' + b[j+1:]
    return b
def f2(b,j):
    b=b[:j] + '+' + b[j+1:]
    return b
print "enter the name of the share"
a=raw_input()
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


for i in range(0,l):
    if(a[i]==" "):
        l1.append(i)
l2=len(l1)
for i in range(0,l2):
    c=f1(a,l1[i])
    a=c
for i in range(0,l2):
    c=f1(a,l1[i])
    a=c
for i in range(0,l2):
    d=f2(a,l1[i])
    a=d
print c
print d




u="http://money.rediff.com/companies/%s/%f?srchword=%s.&snssrc=sugg" %(c,v,d)
page = requests.get(u) 
soup = BeautifulSoup(page.content, "lxml")
for q in soup.find_all('a',target='_jbpinter',rel='nofollow'):
    print q.text












