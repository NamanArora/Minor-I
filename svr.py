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


def predict_price(times,prices,target):
	x = np.transpose(np.matrix(times))
	print x
	y = np.transpose(np.matrix(prices))
	print y

	svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
	svr_lin = SVR(kernel= 'linear', C= 1e3)
	svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
	
	svr_rbf.fit(x, price) # fitting the data points in the models
	# print 'done 1'
	# svr_poly.fit(x, price)
	# print 'done 2'
	
	return svr_rbf.predict(x)[0]

get_data('Ashok Leyland Ltd') # calling get_data method by passing the csv file to it


predicted_price = predict_price(times, price, 29)  
print "\nThe stock open price for 29th Feb is:"
print "RBF kernel: $", str(predicted_price)
print "Linear kernel: $", str(predicted_price[1])
print "Polynomial kernel: $", str(predicted_price[2])
	 