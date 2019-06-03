####################################
# Date: 4-9-2019
# Author: Jason Eisele
# Email : jason.eisele@daimler.com
####################################

import numpy as np
from flask import Flask, abort, jsonify, request
import pickle

my_random_forest = pickle.load(open("iris_rfc.pkl", 'rb'))

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def home():
    return "Hey Birmingham Data Meetup"

@app.route('/ml_api', methods = ['POST'])
def make_predict():
    #######all kinds of error checking should go here#######
    data = request.get_json(force = True)
    #Parse our request json into a list of values
    predict_request = [data['sl'], data['sw'], data['pl'], data['pw']]
    #Convert our list to a numpy array
    predict_request = np.array(predict_request)
    #Reshape into 1d array
    predict_request = predict_request.reshape(1, -1)
    #Assign prediction value to y_hat
    y_hat = my_random_forest.predict(predict_request)
    #Return our prediction to the user
    output = {'y_hat': str([y_hat[0]])}
    return  jsonify(results = output)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)
