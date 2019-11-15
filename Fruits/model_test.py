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
PATH_TO_TRAINED_MODEL_FILE = './Fruits/model/' + MODEL_FILENAME + '.h5'
# PATH_TO_TRAINED_MODEL_FILE = MODEL_FILENAME + '.h5'
test_dir_path = os.path.join('./data/','test')
INPUT_SHAPE = (224, 224, 3)
TARGET_SIZE = INPUT_SHAPE[:2]


def predictFruitClass(ImagePath, trainedModel, class_dict):

    x = image.load_img(ImagePath, target_size=TARGET_SIZE)
    x = image.img_to_array(x)

    plt.imshow((x).astype(np.uint16))
    x = np.expand_dims(x, axis=0)

    prediction_class = trainedModel.predict_classes(x, batch_size=1)
    prediction_probs = trainedModel.predict_proba(x, batch_size=1)
    print('probabilities:',prediction_probs)
    print('class_index:',prediction_class[0])

    for key, value in class_dict.items():
        if value == prediction_class.item():
            return key
    return None
  
def getTrainedModel(PATH_TO_TRAINED_MODEL_FILE):

    trainedModel = load_model(PATH_TO_TRAINED_MODEL_FILE)
    return trainedModel


def results():
    trained_model_path = PATH_TO_TRAINED_MODEL_FILE
    trained_model = getTrainedModel(trained_model_path)
    class_dict = np.load('./Fruits/class_dict.npy', allow_pickle=True).item()

    image_path = './Fruits/data/test/test/ro1.jpg'

    single_pred = predictFruitClass(image_path,trained_model, class_dict)
    return(single_pred)




