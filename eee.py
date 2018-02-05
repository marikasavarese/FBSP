import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
URL="http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"

class LRegression():
    def __init__(self, URL):
       self.URL =URL

    def importAlldata(self):
       return  pd.read_csv(self.URL,parse_dates=['Date'])

    def setX(self):
       X=self.importAlldata()["Date"].apply(lambda x: x.toordinal()).reshape(len(self.importAlldata()["Date"]),1)
       return X

    def setX3d(self):
       X_3d = []
       for i in range(1,4):
          ele=self.importAlldata()["Date"][0]+np.timedelta64(i, 'D')
          X_3d.append(ele.toordinal())
       X_3d = np.reshape(X_3d, (len(X_3d),1))
       return X_3d
 
    def setY(self):
       y=self.importAlldata()["Close"].reshape((len(self.importAlldata()["Close"]),1))
       return y 
      
    def modelFullSet(self):
       linreg=LinearRegression()
       linreg.fit(self.setX(), self.setY())
       y_pred_full=linreg.predict(self.setX())
       return y_pred_full
 
    def model3d(self):
       linreg=LinearRegression()
       linreg.fit(self.setX(), self.setY())
       y_3d=np.round(linreg.predict(self.setX3d()),2)
       return type(y_3d)
 

    def modelMAE(self):
       MAE=np.round(metrics.mean_absolute_error(self.setY(), self.modelFullSet()),decimals=2)
       return MAE

    def modelScore(self):
       SCORE=np.round(metrics.r2_score(self.setY(), self.modelFullSet()),decimals=2)
       return SCORE 
      

       
mydata=LRegression(URL)
print(mydata.model3d())




