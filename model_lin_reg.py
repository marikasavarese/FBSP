import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


class LRegression:
    def __init__(self, URL):
       self.URL = URL

    def importAlldata(self):
    #to print coloumn header refer to print(pdData.coloumns.values)
    #['Symbol' 'Date' 'Open' 'High' 'Low' 'Close' 'Volume' 'Change' '% Change']
       return  pd.read_csv(self.URL,parse_dates=['Date'])

    def setX(self):
    #set the X data
    #we apply the method toordinal to convert the date and reshape to the serie
       X=self.importAlldata()["Date"].apply(lambda x: x.toordinal()).reshape(len(self.importAlldata()["Date"]),1)
       return X

    def setX3d(self):
    #set the X 3 days data
       X_3d = []
       for i in range(1,4):
          ele=self.importAlldata()["Date"][0]+np.timedelta64(i, 'D')
          X_3d.append(ele.toordinal())
       X_3d = np.reshape(X_3d, (len(X_3d),1))
       return X_3d
 
    def setY(self):
    #set the Y data, we apply the method reshape to the serie
       y=self.importAlldata()["Close"].reshape((len(self.importAlldata()["Close"]),1))
       return y 
      
    def modelFullSet(self):
    #setting of a linear regression
    #Remove dieses if you want to check how the model behave with a splitted train/test dataset
    # split the full dataset in train/test default value 80/20, random state is set for reproducinf the splitting procedure
    #X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=1)
    #print(X_train.shape)
    # we train the model on X_train, y_train series
    #linreg.fit(X_train, y_train)
    #we predict values associated to X_test
    #y_pred = linreg.predict(X_test)
    #we print MAE and RMSE with 2 decimal places
    #print("On the test/split 80/20 MAE=", np.round(metrics.mean_absolute_error(y_test, y_pred),decimals=2))
    #print("On the test/split 80/20 RMSE=", np.round(np.sqrt(metrics.mean_squared_error(y_test, y_pred)),decimals=2))
       linreg=LinearRegression()
    #let's train the model on the whole dataset
       linreg.fit(self.setX(), self.setY())
       y_pred_full=linreg.predict(self.setX())
       return y_pred_full
 
    def model3d(self):
       linreg=LinearRegression()
       linreg.fit(self.setX(), self.setY())
    #let's predict on the X_3d data:
       y_3d=np.round(linreg.predict(self.setX3d()), decimals=2)
       return y_3d
 

    def modelMAE(self):
    #MAE=mean average error
       MAE=np.round(metrics.mean_absolute_error(self.setY(), self.modelFullSet()),decimals=2)
       return MAE

    def modelScore(self):
    #score is a method of metrics which computes the r2 the coefficient of determination for a linear regression
       SCORE=np.round(metrics.r2_score(self.setY(), self.modelFullSet()),decimals=2)
       return SCORE 
      
