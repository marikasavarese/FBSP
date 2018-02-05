import pandas as pd
from DateService import *
#here we define a class which given an url as argument of an object:
#1 extract all data and store them in allData
#2 built a list of lists (named table composed of index, Date, Close columns) that we will inject in the HTML code
class data:
    def __init__(self, URL):
      self.URL=URL

    def getCurrentURL(self, URL):
      mydataservice=DateService()
      return URL.replace('[month]', str(mydataservice.getCurrentMonth())).replace('[year]', str(mydataservice.getCurrentYear()))

    def importAlldata(self):
       return  pd.read_csv(self.getCurrentURL(self.URL),parse_dates=['Date'])

    def importData(self):
       allData=self.importAlldata()
       X = allData['Date'].tolist()
       y = allData['Close'].tolist()
       ind = list(range(0, len(allData)))
       table= [[],[],[]]
       for i in range(len(ind)):
           table[0].append(ind[i])
           table[1].append(X[i].strftime('%Y.%m.%d'))
           table[2].append((round(float(y[i]),2)))
       return table
           

