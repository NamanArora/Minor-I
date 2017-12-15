import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def recommendation():
    
        head=[]
        data=[]
        url="http://money.rediff.com/companies/market-capitalisation?src=all_pg"
        A=[]
        B=[]
        C=[]
        D=[]
        res=requests.get(url)
        soup=BeautifulSoup(res.content,"lxml")
        right_table = soup.find('table',class_='dataTable')
        #print (right_table)




        for row in right_table.find_all('tr')[1:6]:
            data = row.findAll('td')
            if len(data)==7: 
                A.append(data[0].find('a',text=True).string)
                B.append(data[1].find(text=True))
                C.append(data[2].find('span',text=True).string)

        for i in range(0,5):
            A[i]=A[i].replace('\t','')
            A[i]=A[i].replace('\n','')
            C[i]=C[i].replace(' ','')

        
        df=pd.DataFrame(A,columns=['Company'],index=['1','2','3','4','5'])
        df['Price']=B
        df['% Change']=C
        print(df)

            
        

       








