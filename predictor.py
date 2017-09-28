from price import crawl
import csv
import datetime
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn import linear_model
import numpy as np

##Linear regression
times=[]
price=[]

def predict_linear_regression(times,prices,target):
    linear_mod = linear_model.LinearRegression()
    x = np.transpose(np.matrix(times))
    y = np.transpose(np.matrix(price))
    linear_mod.fit(x,y)
    predicted_price = linear_mod.predict(target)
    return predicted_price[0][0]
    

def gen_path(sharename,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(sharename)))
    print path
    return path


def convert_to_secs(time_d, show=False):
    times = map(int, re.split(r"[:,]", time_d))
    sum= times[0]*3600+ times[1]*60
    if show:
        print sum
    return sum

def get_data(sharename):
    path=gen_path(sharename)
    with open(path,"r") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            times.append(convert_to_secs(row[0]))
            price.append(float(row[1]))


sharename = raw_input("Enter share name: ")
time = raw_input("Enter the time at which you want to predict: ")

get_data(sharename)
print predict_linear_regression(times,price,convert_to_secs(time,True))