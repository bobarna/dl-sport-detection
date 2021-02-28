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

for label in labels:
    print(label)
print("Number of different sports labels: ", len(labels))
