from flask import Flask,request

import os
app = Flask(__name__)



## Keras
import scipy
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import scipy
from PIL import Image
import numpy as np
from keras_contrib.layers.normalization import InstanceNormalization



@app.route('/')
def hello():
    return 'Hello Container World!'

@app.route('/gen',methods =  ['GET','POST'])
def gen():
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form # a multidict containing POST data
    
        return 'Hello Container World gen!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
