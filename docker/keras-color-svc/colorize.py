from flask import Flask

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
