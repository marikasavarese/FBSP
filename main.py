from flask import * 
import numpy, pandas, sklearn 
from model_lin_reg import LRegression 
from  ImportData import data

#change here URL of CSV file if you want to change data (WARNING check coloumn header in Importdata)
url="http://markets.financialcontent.com/stocks/action/gethistoricaldata?Symbol=537%3A14917609&Month=1&Range=12&Year=2018"


app = Flask(__name__)

@app.route('/result')
def result():
    mydata = LRegression(url)
    return render_template('result.html', values=mydata.model3d(), mae=mydata.modelMAE(), score=mydata.modelScore(), url=Markup(url))


@app.route('/table')
def table():
    mydata = data(url)
    return render_template('table.html', result=mydata.importData())

if __name__ == '__main__':
   app.run(debug = True)



