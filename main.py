from flask import * 
import numpy, pandas, sklearn 
from model_lin_reg import LRegression 
from  ImportData import data

#change here URL of CSV file if you want to change data (WARNING check coloumn header in Importdata)
url="http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=[month]&Range=12&Year=[year]"


app = Flask(__name__)

@app.route('/result')
def result():
    importdata = data(url)
    mydata = LRegression(importdata.getCurrentURL(url))
    return render_template('result.html', values=mydata.model3d(), mae=mydata.modelMAE(), score=mydata.modelScore(), url=Markup(importdata.getCurrentURL(url)))


@app.route('/table')
def table():
    mydata = data(url)
    return render_template('table.html', result=mydata.importData())

if __name__ == '__main__':
   app.run(debug = True)



