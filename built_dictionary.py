import pandas as pd
import numpy as np

def generateTable():
    URL = "http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"

    pdData = pd.read_csv(URL, parse_dates=['Date'])

    table = [[],[],[]]

    #set the X data
    X_list = []
    X = pdData["Date"]
    i=0
    for ele in X:
        d = ele.strftime('%Y.%m.%d')
        table[0].append(i)
        table[1].append(d)
        i+=1

    #set the y data
    y_list = []
    y = pdData["Close"]
    for ele in y:
        table[2].append(round(float(ele),2))


    return table

