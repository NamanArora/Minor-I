from price import crawl
import csv
import datetime
import os
import time
import pandas as pd
import matplotlib.pyplot as plt

##Linear regression
times=[]
price=[]

def gen_path(sharename,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(sharename)))
    print path
    return path


def get_data(sharename):
    path=gen_path(sharename)
    with open(path,"r") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            times.append(float(row[0]))
            price.append(float(row[1]))


sharename = raw_input("Enter share name: ")
get_data(sharename)
print times
print price