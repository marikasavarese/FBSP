from flask import * 
import numpy, pandas 
from built_dictionary import results
from model_lin_reg import regression_model

app = Flask(__name__)

@app.route('/result')
def result():
    dict = results()
    predicted = [] 
    predicted = regression_model()
    return render_template('result.html', result = dict, pred = predicted)

if __name__ == '__main__':
   app.run(debug = True)
