from flask import * 
import numpy, pandas, sklearn 
from model_lin_reg import regression_model
from built_dictionary import generateTable

app = Flask(__name__)

@app.route('/result')
def result():
    test =generateTable()
    predicted = [] 
    predicted = regression_model()
    indexes   = (list(range(0,250)))
    return render_template('result.html', result=test, pred=predicted, ind=indexes)

if __name__ == '__main__':
   app.run(debug = True)


