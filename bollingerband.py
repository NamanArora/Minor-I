import csv
import datetime
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    return pd.rolling_std(values,window=window)


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm + rstd*2 
    lower_band = rm - rstd*2 
    return upper_band, lower_band


def get_data(symbols, dates):
        df = pd.DataFrame(index=dates)
        for symbol in symbols:
              temp = pd.read_csv(gen_path(symbol) , index_col='Date', parse_dates=True, na_values=['nan'], usecols=['Date', 'Price'])        
              temp = temp.rename(columns={'Price': symbol})
              df = df.join(temp, how='inner')

        return df


def gen_path(sharename,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(sharename)))
    return path



def val(sharename):
    path=gen_path(sharename)
    with open(path,'r') as file:
        
        
        content = []
        reader = csv.reader(file)
        next(reader)
        included_cols = [1]
        for row in reader:
            content.append(row[1])
        return content

def dat(sharename):
    path=gen_path(sharename)
    with open(path,'r') as file:
        
        
        content = []
        reader = csv.reader(file)
        next(reader)
        included_cols = [0]
        for row in reader:
            content.append(row[0])
        return content






def fun(sharename):

    shares = []
    shares.append(sharename)
    dates = pd.date_range("09:00","15:30", freq="1min")    
     
    df = get_data(shares,dates)
        # Compute Bollinger Bands
        # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df[shares[0]], window=20)

        # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df[shares[0]], window=20)

        # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    #plotting of the dataframe of the share
    ax = df[shares[0]].plot(title="Bollinger Bands", label=shares[0])

    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


    p=val(sharename)
    d=dat(sharename)
   
    ub=[]
    lb=[]
    ub = upper_band
    lb = lower_band

    
    print" "
    print"          SELLING OF SHARE          "

    mx=float(p[20])
    for i in range(20,len(ub)-1):
        if(float(p[i+1])>mx):
            mx=float(p[i+1])
            ix=i+1
    print"MAXIMUM VALUE OF SHARE IS %d AT THIS TIME %s" %(mx,d[ix])    
        
    print'.................................................'
    print'.................................................'


    print"           BUYING OF SHARE            "
    mn=float(p[20])
    for i in range(20,len(lb)-1):

        if(float(p[i+1])<mn):
            mn=float(p[i+1])
            ix=i+1
    print"MINIMUM VALUE OF SHARE IS %d AT THIS TIME %s" %(mn,d[ix])


    










