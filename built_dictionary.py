import pandas as pd
import numpy as np

def results():
    URL = "http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"

    pdData = pd.read_csv(URL, parse_dates=['Date'])


    #set the X data
    X_list = []
    X = pdData["Date"]
    for ele in X:
        d = ele.strftime('%Y.%m.%d')
        X_list.append(d)

    #set the y data
    y_list = []
    y = pdData["Close"]
    for ele in y:
        y_list.append(ele)


    dictionary = dict(zip(X_list,y_list))

    return dictionary

