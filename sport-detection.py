#!/usr/bin/python3
import os
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import cv2 
import numpy as np

from tensorflow import keras
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img

# Generating Label list from first-level subfolders of the data folder

# data directory path
data_dir = './data'

# first-level subfolders in the data directory
labels = [ item for item in sorted(os.listdir(data_dir)) if
           os.path.isdir(os.path.join(data_dir, item)) ]

# TODO validate label names

# for label in labels:
#     print(label)
print("Number of different sports labels: ", len(labels))


label_dir_paths = []
for l in labels:
    label_dir_paths.append(os.path.join(data_dir, l))

# generating list of image paths
# path of images
X_paths = []
# label of the image
Y = []

# Filling up the path for X values
# Filling up the Y values
for label_dir in label_dir_paths:
    # strips everything before the last part of the path
    curr_label = os.path.basename(os.path.normpath(label_dir))
    # scandir returns the files in arbitrary order
    for img in os.scandir(label_dir):
        X_paths.append(img.path)
        # array of: 1 for its label, 0 for other labels
        Y.append([1 if curr_label==l else 0 for l in labels])

# print path of image -> [0... 1 ...0]
# for i in range(len(X_paths)):
#     print(X_paths[i] + " -> " + str(Y[i]))

X = []
# Fill X values
counter = 0
for curr_image in X_paths:
    if (
        curr_image.split(".")[-1] != "jpg" and
        curr_image.split(".")[-1] != "jpeg" and
        curr_image.split(".")[-1] != "png" 
            ):
            continue
    X.append(
        cv2.resize( 
            cv2.imread(curr_image, cv2.IMREAD_COLOR), 
            (64,64),
            interpolation=cv2.INTER_CUBIC 
        )
    )
    if counter %1000 ==0:
      print(counter)
    counter +=1


# Convert to numpy array
X = np.array(X)
Y = np.array(Y)
print('Shape of image is: {}'.format(X.shape))
print('Shape of labels is: {}'.format(Y.shape))
