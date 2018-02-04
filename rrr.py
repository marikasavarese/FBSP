import pandas as pd
#here we define a class which given an url as argument of an object:
#1 extract all data and store them in allData
#2 built a list of lists (named table composed of index, Date, Close columns) that we will inject in the HTML code
class data:
    def __init__(self, URL):
       self.URL = URL 

    def import_alldata(self):
       allData=pd.read_csv(self.URL,parse_dates=['Date'])
       return allData

    def import_data(self):
       allData=pd.read_csv(self.URL,parse_dates=['Date'])
       X = allData['Date'].tolist()
       y = allData['Close'].tolist()
       ind = list(range(0, len(allData)))
       table= [[],[],[]]
       for i in range(len(ind)):
           table[0].append(ind[i])
           table[1].append(X[i].strftime('%Y.%m.%d'))
           table[2].append((round(float(y[i]),2)))
       return table
           
