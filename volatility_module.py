import os
import numpy as np
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def volatility(dirname_inp, year_beg, month_beg, day_beg, year_end, month_end, day_end):

    dirname = os.fsencode(dirname_inp)
    timestamp_format = "%Y%m%d"
    start_date = datetime.strptime(f"{year_beg}{month_beg}{day_beg}", timestamp_format)
    end_date = datetime.strptime(f"{year_end}{month_end}{day_end}", timestamp_format)

    timestamps = []
    close_prices = np.array([])

    for file in os.listdir(dirname):
        fullpath = dirname + b'\\' + file
        filename = os.fsdecode(file)
        date = (filename.split('_')[1])[:-4]
        date = datetime.strptime(date, timestamp_format)
        if date < start_date:
            continue
        if date > end_date:
            break
        df = pd.DataFrame()
        with open(fullpath) as csv_file:
            df = pd.read_csv(csv_file, delimiter=';')
        for _, row in df.iterrows():
            timestmp = datetime.strptime(row.iloc[1], "%Y-%m-%dT%H:%M:%SZ")
            close_pr = row.iloc[5] # Close prices
            timestamps.append(timestmp)
            close_prices = np.append(close_prices, close_pr)
        
    df = pd.DataFrame({'Date': pd.to_datetime(timestamps), 'Close': close_prices})
    df = df.set_index(['Date'])
    df_range = df[start_date:end_date]

    expected_return = np.mean(df_range['Close'])
    volat = np.std(df_range['Close'])

    return (expected_return, volat, df_range)

def volatility(dirname_inp, date_beg, date_end):

    (year_beg, month_beg, day_beg) = date_beg
    (year_end, month_end, day_end) = date_end

    dirname = os.fsencode(dirname_inp)
    timestamp_format = "%Y%m%d"
    start_date = datetime.strptime(f"{year_beg}{month_beg}{day_beg}", timestamp_format)
    end_date = datetime.strptime(f"{year_end}{month_end}{day_end}", timestamp_format)

    timestamps = []
    close_prices = np.array([])

    for file in os.listdir(dirname):
        fullpath = dirname + b'\\' + file
        filename = os.fsdecode(file)
        date = (filename.split('_')[1])[:-4]
        date = datetime.strptime(date, timestamp_format)
        if date < start_date:
            continue
        if date > end_date:
            break
        df = pd.DataFrame()
        with open(fullpath) as csv_file:
            df = pd.read_csv(csv_file, delimiter=';')
        for _, row in df.iterrows():
            timestmp = datetime.strptime(row.iloc[1], "%Y-%m-%dT%H:%M:%SZ")
            close_pr = row.iloc[5] # Close prices
            timestamps.append(timestmp)
            close_prices = np.append(close_prices, close_pr)
        
    df = pd.DataFrame({'Date': pd.to_datetime(timestamps), 'Close': close_prices})
    df = df.set_index(['Date'])
    df_range = df[start_date:end_date]

    expected_return = np.mean(df_range['Close'])
    volat = np.std(df_range['Close'])

    return (expected_return, volat, df_range)

def plotClosePrices(df_range, prompt):
    if prompt:
        q = input("Would you like to see the plot? [Y/n] ")
    else:
        q = 'Y'
    if q == 'n':
        return
    elif q != 'Y' and q != 'y' and q != '':
        print("Sorry, that was unintelligible. Please try once again")
        return plotClosePrices(df_range)
    resampled_data = df_range.resample('30min').mean()
    your_ticker = input("What is the company ticker? ")
    # print(test)
    plt.figure(figsize=(14,5))
    sns.set_style("ticks")
    plt.plot(resampled_data.index, resampled_data['Close'])
    sns.lineplot(resampled_data, x="Date", y="Close", color="firebrick")
    sns.despine()
    plt.title(f"The Stock Price of {your_ticker}",size='x-large',color='blue')
    plt.show()

def plotClosePrices(df_range, prompt, name = None):
    if prompt:
        q = input("Would you like to see the plot? [Y/n] ")
    else:
        q = 'Y'
    if q == 'n':
        return
    elif q != 'Y' and q != 'y' and q != '':
        print("Sorry, that was unintelligible. Please try once again")
        return plotClosePrices(df_range)
    resampled_data = df_range.resample('30min').mean()
    if name == None:
        your_ticker = input("What is the company ticker? ")
    else:
        your_ticker = name
    # print(test)
    plt.figure(figsize=(14,5))
    sns.set_style("ticks")
    plt.plot(resampled_data.index, resampled_data['Close'])
    sns.lineplot(resampled_data, x="Date", y="Close", color="firebrick")
    sns.despine()
    plt.title(f"The Stock Price of {your_ticker}",size='x-large',color='blue')
    if prompt:
        plt.show()

def plotClosePrices(df_range, prompt, name = None,):
    if prompt:
        q = input("Would you like to see the plot? [Y/n] ")
    else:
        q = 'Y'
    if q == 'n':
        return
    elif q != 'Y' and q != 'y' and q != '':
        print("Sorry, that was unintelligible. Please try once again")
        return plotClosePrices(df_range)
    resampled_data = df_range.resample('30min').mean()
    if name == None:
        your_ticker = input("What is the company ticker? ")
    else:
        your_ticker = name
    # print(test)
    plt.figure(figsize=(14,5))
    sns.set_style("ticks")
    plt.plot(resampled_data.index, resampled_data['Close'])
    sns.lineplot(resampled_data, x="Date", y="Close", color="firebrick")
    sns.despine()
    plt.title(f"The Stock Price of {your_ticker}",size='x-large',color='blue')
    if prompt:
        plt.show()