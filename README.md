# WhatMonthIsTheBestTimeToBuyStocks
This quick script tells us the best month on average to buy stocks. You can customize this for your symbol and backdate it as far as you'd like. 

## Results:

When testing this code on VOO and a couple of other stocks, the general best months to buy stocks are February, July, October, and November, with  Nov and Feb being the better months to do so.

There are many lurking variables, and the variance in these results is relatively high. Please take this with a grain of salt. Past performance is not indicative of future performance, but it can be a significant key to helping us better understand the world around us.


## How to change the symbol you want to analyze
In the function CalculateByMonth, look at line 30. This line calls the function MonthlyAnalysis(), and the first parameter is the symbol. Feel free to change this to any symbol you can find on Yahoo Finance, as this program depends on the yfinance package.

## How to change the date range you want to analyze

Look at line 21. The range function is just a for loop that counts from the initial year to the final year but excludes the last year (For example, if you said for year in range (2022,2020,-1), you would see only 2022 and 2021 in there, but not 2020. The -1 in the third parameter tells you you are going down one year at a time. If you'd instead look at every other year, you can set the third parameter to -2, or if you want, every three years, you just put the third parameter to -3. 
