from flask import Flask,request,url_for, send_from_directory
from werkzeug.datastructures import ImmutableMultiDict
import os,sys
app = Flask(__name__)
from werkzeug import secure_filename


## Keras
import scipy
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import scipy
from PIL import Image,ImageEnhance
import numpy as np
from keras_contrib.layers.normalization import InstanceNormalization
import tensorflow as tf
import cv2
global model,prep
model = load_model('./models/gen_model2.h5')
model.load_weights('./models/gen_weights2.h5')

prep = load_model('./models/gen_model2.h5')
prep.load_weights('./models/gen_prep.h5')
global graph 
graph = tf.get_default_graph()


def imread(path):
        return scipy.misc.imfilter(scipy.misc.imfilter(scipy.misc.imread(path, mode='RGB').astype(np.float),ftype='smooth_more'),ftype='smooth')

def imprep(path) : 
        c = imread(path)
        c = scipy.misc.imresize(c, (128, 128))
        c = np.array(c)/125.5 - 1.#edges
        c = np.expand_dims(c, axis=0)
        return  c

# END keras 
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
_IP = "http://localhost:5000/"
app.config['upload'] = os.path.join("upload")
app.config['conv']  = os.path.join("conv")
@app.route('/')
def hello():
    return 'Hello Container World!'

@app.route('/gen',methods =  ['POST'])
def gen():
    print("got request")
    if request.method == 'POST':
        file = request.files['file']
        if file :
            print ('**found file', file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload'], filename))
            img= cv2.imread(os.path.join(app.config['upload'], filename))
            height, width,alp = img.shape
            #print (height, width,alp)
            im =imprep(os.path.join(app.config['upload'], filename))

 
        with graph.as_default():
                
                prep2 = prep.predict(im)
                im=im/2 + prep2 /2
                colorize = model.predict(im)
                color =scipy.misc.imresize( np.concatenate(colorize),(height,width))
                color = scipy.ndimage.median_filter(color,3 );
                 
                scipy.misc.imsave( "./conv/color-"+file.filename,  color)
                img = Image.open( "./conv/color-"+file.filename)
                converter = ImageEnhance.Color(img)
                img2 = converter.enhance(2)
                img2.save("./conv/color-"+file.filename)
                return _IP+"upload/"+file.filename+','+_IP+'conv/color-'+file.filename

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
