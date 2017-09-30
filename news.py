from bs4 import BeautifulSoup
import requests
import string
import os
import csv
import re

good_dict=[]
bad_dict=[]

def gen_path(file_name,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(file_name)))
    return path

def fill_dict():
    path=gen_path('dictionary')
    with open(path,'r') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for row in file_reader:
            good_dict.append(row[0])
            bad_dict.append(row[1])


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
if(a=="Mahindra Mahindra Financial Services Ltd"):
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



news=[]
u="http://money.rediff.com/companies/%s/%f?srchword=%s.&snssrc=sugg" %(c,v,d)
page = requests.get(u) 
soup = BeautifulSoup(page.content, "lxml")
for q in soup.find_all('a',target='_jbpinter',rel='nofollow'):
    news.append(q.text)
    print q.text

score =0
fill_dict()
for i in news:
    t=i.split(' ')
    for word in good_dict:
        if word in t:
            score = score +1
            print 'good='+word
    for word in bad_dict:
        if word in t:
            score = score -1
            print 'bad='+word


if score == 0:
    print 'Prediction: Your stock will remain stable'
elif score>0:
    print 'Prediction: Your stock will rise'
elif score<0:
    print 'Prediction: Your stock will fall'















