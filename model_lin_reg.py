import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def regression_model():
    URL = "http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"
   
    pdData = pd.read_csv(URL, parse_dates=['Date'])
    #to print coloumn header refer to print(pdData.coloumns.values)
    #['Symbol' 'Date' 'Open' 'High' 'Low' 'Close' 'Volume' 'Change' '% Change']
   
   
    #set the X data
    #we apply the method toordinal to convert the date and reshape to the serie
    X = pdData["Date"].apply(lambda x: x.toordinal()).reshape(len(pdData["Date"]),1)
   
    #set the X 3 days data
    X_3d = []
   
    for i in range(1,4):
       ele=pdData["Date"][0]+np.timedelta64(i, 'D')
       X_3d.append(ele.toordinal())
   
    X_3d = np.reshape(X_3d, (len(X_3d),1))
   
    #set the Y data, we apply the method reshape to the serie
    y = pdData["Close"].reshape((len(pdData["Close"]),1))
   
    #setting of a linear regression
    linreg = LinearRegression()
   
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
   
   
    #let's train the model on the whole dataset
    linreg.fit(X,y)
    y_pred_full = linreg.predict(X)
    #print("On the entire dataset MAE=", np.round(metrics.mean_absolute_error(y, y_pred_full),decimals=2))
    #print("On the entire dataset RMSE=", np.round(np.sqrt(metrics.mean_squared_error(y, y_pred_full)),decimals=2))
   
    #let's predict on the X_3d data:
    y_3d = linreg.predict(X_3d)
   
    for i in range(len(y_3d)):
        y_3d[i] =round(float(y_3d[i]),2)
    
#   remove comment if you want to compute the RMSE
#   RMSE=np.round(np.sqrt(metrics.mean_squared_error(y, y_pred_full)),decimals=2)
#   RMSE=np.reshape(RMSE,(1,1))
    MAE=np.round(metrics.mean_absolute_error(y, y_pred_full),decimals=2)
    SCORE=np.round(metrics.r2_score(y, y_pred_full),decimals=2)
    MAE=np.reshape(MAE,(1,1))
    SCORE=np.reshape(SCORE,(1,1))
    y_3d_all=np.concatenate((y_3d, MAE,SCORE), axis=0)  

    return y_3d_all
