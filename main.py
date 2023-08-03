import pandas as pd
import os
import yfinance as yf
from datetime import datetime
import numpy as np
import calendar

def MonthlyAnalysis(symbol, start_date, end_date):
    fund = yf.download(symbol, start=start_date, end=end_date, progress=False)
    initial_price = fund['Close'][0]  # Closing price on start_date
    current_price = fund['Close'][-1]  # Last available closing price
    percentage_return = (current_price - initial_price) / initial_price * 100
    return percentage_return

def calculateByMonth():
    results = {}

    for month in range(12,0,-1):
        results[month] = []

    for year in range(2022,2011,-1):
        for month in range(12,0,-1):
            start_date = datetime(year, month, 1)

            if month == 12:
                end_date = datetime(year+1, 1, 1)
            else:
                end_date = datetime(year, month+1, 1)

            results[month].append(MonthlyAnalysis('VOO',start_date,end_date))
    return results


if __name__ == "__main__":
    results = calculateByMonth()
    print(results)

    # for month in results:
    #     average = np.mean(results[month])
    #     print(f"Average % Return for month {month}:  {average}")

