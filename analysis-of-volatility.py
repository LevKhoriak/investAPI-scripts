import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from volatility_module import volatility, plotClosePrices

dirname_inp = input("What is the path to your CSV files ")
print("Firstly input the start date for the analysis")
year_beg = input("year (ex. 2022): ")
month_beg = input("month (ex. 01): ")
day_beg = input("day (ex. 05): ")
print("Now input the end date")
year_end = input("year (ex. 2022): ")
month_end = input("month (ex. 01): ")
day_end = input("day (ex. 05): ")


dirname = os.fsencode(dirname_inp)
timestamp_format = "%Y%m%d"
start_date = datetime.strptime(f"{year_beg}{month_beg}{day_beg}", timestamp_format)
end_date = datetime.strptime(f"{year_end}{month_end}{day_end}", timestamp_format)

(ex, var, df_range) = volatility(dirname_inp, year_beg, month_beg, day_beg, year_end, month_end, day_end)

print(f"Expected value is {ex}, volatility is {var}")

plotClosePrices(df_range)