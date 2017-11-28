import csv
import os
import pandas as pd
import time
from price import crawl
import datetime
import string
def create_csv_file(sharename):
    titles=['Date','Price']
    
    path=gen_path(sharename)
    if os.path.exists(path):
        pass
    else:
        with open(path,"w") as file:
            wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
            wr.writerow(titles)

    t_end= time.time() + 21600
    while time.time() < t_end:
        p = crawl(sharename)
        shareprice = string.replace(p,',','')
        print float(shareprice)
        now=datetime.datetime.now()
        with open(path,'a') as file:
            wr=csv.writer(file)
            wr.writerow([now.strftime("%H:%M"),shareprice])
        time.sleep(60)


def gen_path(symbol , base_dir= 'data'):
    path = os.path.join(base_dir, '{}.csv'.format(str(symbol)))
    print path
    return path

sharename = raw_input("Enter share name: ")

create_csv_file(sharename)
