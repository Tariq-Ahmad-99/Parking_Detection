import numpy as np 
import os
from tensorflow.keras import applications # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras import optimizers  # type: ignore
from tensorflow.keras.models import Sequential, Model # type: ignore
from tensorflow.keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D # type: ignore


files_train = 0
files_validation = 0
cwd = os.getcwd()

# train data
folder = 'data/train'

for sub_folder in os.listdir(folder):
    path, dirs, files = next(os.walk(os.path.join(folder, sub_folder)))
    files_train += len(files)

# test data
folder = 'data/test'

for sub_folder in os.listdir(folder):
    path, dirs, files = next(os.walk(os.path.join(folder, sub_folder)))
    files_validation += len(files)


## Set Key Parameters 

img_width, img_height = 48,48
train_data_dir = 'data/train'
validation_data_dir = 'data/test'
nb_train_sample = files_train
nb_validation_sample = files_validation
batch_size = 32
epochs = 10
num_classes = 2

## build the CNN-VGG Model