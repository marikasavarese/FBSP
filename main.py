from flask import * 
import numpy, pandas, sklearn 
from model_lin_reg import regression_model
from  ImportData import data

#change here URL of CSV file if you want to change data (WARNING check coloumn header in Importdata)
url="http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"


app = Flask(__name__)

@app.route('/result')
def result():
    mydata = data(url)
    test =mydata.import_data()
    predicted = [] 
    predicted = regression_model()
    return render_template('result.html', result=test, pred=predicted)

if __name__ == '__main__':
   app.run(debug = True)


