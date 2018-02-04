from  model_lin_reg2 import Linear_regression
url="http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"
mydata = Linear_regression(url)
table=mydata.MAE()
print(table)
