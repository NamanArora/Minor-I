import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

def create_csv_file(name):
    titles = ['Date','Price']
    path = gen_filename(name)
    #print path
    with open(path,"w") as file:
        wr = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
        wr.writerow(titles)


def gen_filename(symbol , base_dir= 'data'):
    path = os.path.join(base_dir, '{}.csv'.format(str(symbol)))
    print path
    return path


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

def dummy_data(name):
    return


def get_data(symbols, dates):
        df = pd.DataFrame(index=dates)
        for symbol in symbols:
              temp = pd.read_csv(gen_filename(symbol) , index_col='Date', parse_dates=True, na_values=['nan'], usecols=['Date', 'Close'])
              temp = temp.rename(columns={'Close': symbol})
              df = df.join(temp, how='inner')

        return df

# shares=["Larsen Toubro Infotech Ltd", "Indian Oil Corporation Ltd"]
# for share in shares :
#     create_csv_file(share)
#     dummy_data(share)
shares = ['SPY']
dates = pd.date_range('2010-01-01', '2010-12-31')    
df = get_data(shares,dates)
 # Compute Bollinger Bands
    # 1. Compute rolling mean
rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
#rm_SPY.plot(label='Rolling mean', ax=ax)
upper_band.plot(label='upper band', ax=ax)
lower_band.plot(label='lower band', ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend(loc='upper left')
plt.show()
os.system('cls' if os.name == 'nt' else 'clear')