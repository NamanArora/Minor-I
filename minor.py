from price import crawl
import csv
import datetime
import os
import time
import pandas as pd
import matplotlib.pyplot as plt


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


def plot_dataframe(df):
    df.plot()
    plt.show()

def get_data(symbols, dates):
        df = pd.DataFrame(index=dates)
        for symbol in symbols:
              temp = pd.read_csv(gen_path(symbol) , index_col='Date', parse_dates=True, na_values=['nan'], usecols=['Date', 'Price'])
              temp = temp.rename(columns={'Price': symbol})
              df = df.join(temp, how='inner')

        return df


def create_csv_file(sharename):
    titles=['Date','Price']
    
    path=gen_path(sharename)
    if os.path.exists(path):
        pass
    else:
        with open(path,"w") as file:
            wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
            wr.writerow(titles)

    t_end= time.time() + 23400
    while time.time() < t_end:
        p = crawl(sharename)
        shareprice = p
        now=datetime.datetime.now()
        with open(path,'a') as file:
            wr=csv.writer(file)
            wr.writerow([now.strftime("%H:%M"),shareprice])
        time.sleep(60)
    


def gen_path(sharename,base_dir='data'):
    path=os.path.join(base_dir,'{}.csv'.format(str(sharename)))
    print path
    return path



##Enter share name
sharename = raw_input("Enter share name: ")

##Fetch data of that share via crawling
#create_csv_file(sharename)
#get_data(sharename)


shares = []
shares.append(sharename)
dates = pd.date_range("9:00","15:30", freq="1min")    
#dates = pd.date_range("3:20","6:30", freq="1min") 
df = get_data(shares,dates)
 # Compute Bollinger Bands
    # 1. Compute rolling mean
rm_SPY = get_rolling_mean(df[shares[0]], window=2)

    # 2. Compute rolling standard deviation
rstd_SPY = get_rolling_std(df[shares[0]], window=2)

    # 3. Compute upper and lower bands
upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
ax = df[shares[0]].plot(title="Bollinger Bands", label=shares[0])
#rm_SPY.plot(label='Rolling mean', ax=ax)
upper_band.plot(label='upper band', ax=ax)
lower_band.plot(label='lower band', ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend(loc='upper left')
plt.show()













































