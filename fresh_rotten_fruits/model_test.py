import tensorflow as tf
import keras as k
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import h5py
import os
from PIL import Image



MODEL_FILENAME = 'model_fruit_fresh_rotten'
# PATH_TO_TRAINED_MODEL_FILE = 'model/'+MODEL_FILENAME+'.h5'
PATH_TO_TRAINED_MODEL_FILE = MODEL_FILENAME+'.h5'
# PATH_TO_TRAINED_MODEL_FILE = MODEL_FILENAME + '.h5'
# test_dir_path = os.path.join('/data/','test')
INPUT_SHAPE = (224, 224, 3)
TARGET_SIZE = INPUT_SHAPE[:2]


# Fruits/model/model_fruit_fresh_rotten.h5

# def predictFruitClass(ImagePath, trainedModel, class_dict):
def predictFruitClass(img, trainedModel, class_dict):

    x = img
    # included below to resolve ValueError: Error when checking input: expected vgg16_input to have 4 dimensions, but got  array with shape (1, 1)
    # x = x.reshape((-1, 100, 100, 1))

    x = image.img_to_array(x) #ValueError: could not convert string to float:

    plt.imshow((x).astype(np.uint16)) #AttributeError: 'bytes' object has no attribute 'astype'
    # plt.imshow(x) TypeError: Image data of dtype |S5151 cannot be converted to float
    x = np.expand_dims(x, axis=0)

    prediction_class = trainedModel.predict_classes(x, batch_size=1)
    prediction_probs = trainedModel.predict_proba(x, batch_size=1)

    return prediction_class, prediction_probs
  
def getTrainedModel(PATH_TO_TRAINED_MODEL_FILE):

    trainedModel = load_model(PATH_TO_TRAINED_MODEL_FILE)
    return trainedModel

# def results():
def results(img):
    result = {} 
    trained_model_path = PATH_TO_TRAINED_MODEL_FILE
    trained_model = getTrainedModel(trained_model_path)
    class_dict = np.load('class_dict.npy', allow_pickle=True).item()

    # image_path = 'data/test/test/ro5.jpg' im.resize((width, height))
    img_resize = img.resize((224, 224))
    single_pred = predictFruitClass(img_resize, trained_model, class_dict)
    result = single_pred
    return result, class_dict

