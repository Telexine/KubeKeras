from flask import Flask,request,url_for, send_from_directory
from werkzeug.datastructures import ImmutableMultiDict
import os
app = Flask(__name__)
from werkzeug import secure_filename


## Keras
import scipy
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import scipy
from PIL import Image
import numpy as np
from keras_contrib.layers.normalization import InstanceNormalization


app.config['upload'] = "upload"


@app.route('/')
def hello():
    return 'Hello Container World!'

@app.route('/gen',methods =  ['POST'])
def gen():
    print("hello")
    if request.method == 'POST':
        file = request.files['file']
        if file :
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload'], filename))
            # for browser, add 'redirect' function on top of 'url_for'
            print(url_for('uploaded_file',
                                    filename=filename))
            return url_for('uploaded_file',
                                    filename=filename)

        return 'Error'

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['upload'],
                               filename)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
