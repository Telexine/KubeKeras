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
import tensorflow as tf
import cv2
global model
model = load_model('./models/gen_model2.h5')
model.load_weights('./models/gen_weights2.h5')
global graph 
graph = tf.get_default_graph()


def imread(path):
        return scipy.misc.imread(path, mode='RGB').astype(np.float)

def imprep(path) : 
        c = imread(path)
        c = scipy.misc.imresize(c, (128, 128))
        c = np.array(c)/125.5 - 1.#edges
        c = np.expand_dims(c, axis=0)
        return  c

# END keras 

app.config['upload'] = "upload"
app.config['conv'] = "conv"
@app.route('/')
def hello():
    return 'Hello Container World!'

@app.route('/gen',methods =  ['POST'])
def gen():
    print("got request")
    if request.method == 'POST':
        file = request.files['file']
        if file :
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload'], filename))

            img= cv2.imread("upload/"+filename)
            height, width,alp = img.shape
            print height, width,alp
            im =imprep("upload/"+filename)

 
        with graph.as_default():
                colorize = model.predict(im)
         
                color =scipy.misc.imresize( np.concatenate(colorize),(height,width))
                scipy.misc.imsave('conv/color-'+file.filename,  color)

                # for browser, add 'redirect' function on top of 'url_for'
                ori = url_for('uploaded_file',
                                        filename=filename)
                return ori+',conv/color-'+file.filename

        return 'Error'

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['upload'],
                               filename)
@app.route('/conv/<filename>')
def file(filename):
    return send_from_directory(app.config['conv'],
                               filename)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
