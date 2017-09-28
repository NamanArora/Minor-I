from price import crawl
import csv
import datetime
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn import linear_model

##Linear regression
times=[]
price=[]

def predict_linear_regression(dates,prices,x):
    

def gen_path(sharename,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(sharename)))
    print path
    return path


def convert_to_secs(time_d):
    times = map(int, re.split(r"[:,]", time_d))
    return times[0]*3600+ times[1]*60

def get_data(sharename):
    path=gen_path(sharename)
    with open(path,"r") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            times.append(convert_to_secs(row[0]))
            price.append(float(row[1]))


sharename = raw_input("Enter share name: ")
get_data(sharename)
