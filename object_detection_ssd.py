# Ryan L Buchanan - 17AUG2020
# Object Detection with SSD
# Importing the libraries
import torch
from torch.autograd import Variable
import cv2
from data import BaseTransform, VOC_CLASSES as labelmap
from ssd import build_ssd
import imageio