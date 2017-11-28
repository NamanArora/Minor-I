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
    return path

def calc_mean_error():
    a=[]
    acc=0
    for time in times:
        a.append(predict_linear_regression(times,price,time))
    pred = np.array(a)
    actual = np.array(price)
    diff= np.subtract(actual,pred)
    div=np.divide(diff,actual)
    mean= np.mean(div)
    print " "
    print"Error in calculating the Predicted Value in %: "
    print mean*100
    
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


def linereg(sharename):
    get_data(sharename)
    print" "
    print "Enter The Time for Which Price Has To Be Predicted: "
    time=raw_input()
    print " "
    print " Predicted Value Through Linear Regression is: "
    print predict_linear_regression(times,price,convert_to_secs(time))
   
    calc_mean_error()
    






