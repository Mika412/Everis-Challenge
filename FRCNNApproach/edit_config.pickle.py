from __future__ import division
import os
import cv2
import numpy as np
import sys
import pickle
from optparse import OptionParser
import time
from keras_frcnn import config
from keras import backend as K
from keras.layers import Input
from keras.models import Model
from keras_frcnn import roi_helpers

config_output_filename = "config.pickle"
with open(config_output_filename, 'rb') as f_in:
	C = pickle.load(f_in)
print("loaded")
print(C.model_path)