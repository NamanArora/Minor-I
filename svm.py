import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import os
import re
times=[]
price=[]

def gen_path(sharename,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(sharename)))
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
	return

def calc_mean_error():
    a=[]
    acc=0
    for time in times:
        a.append(predict_price(times,price,time))
    pred = np.array(a)
    actual = np.array(price)
    diff= np.subtract(actual,pred)
    div=np.divide(diff,actual)
    mean= np.mean(div)
    return  mean


def predict_price(times,prices,target):
	x = np.transpose(np.matrix(times))
	#print x
	y = np.transpose(np.matrix(prices))
	#print y

	svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
	
	
	svr_rbf.fit(x, prices) # fitting the data points in the models
	
	return svr_rbf.predict(target)[0]

def svmalgo(sharename,time):

    get_data(sharename)
    predicted_price = predict_price(times, price, convert_to_secs(time))
    return str(predicted_price),calc_mean_error()
    

    
    


