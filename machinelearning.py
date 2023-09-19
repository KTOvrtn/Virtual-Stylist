#https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
#https://www.tensorflow.org/tutorials/keras/classification#use_the_trained_model
#https://towardsdatascience.com/fashion-mnist-classification-with-tensorflow-featuring-deepmind-sonnet-aeb3987d826e
#https://www.kaggle.com/code/scratchpad/notebook6d15019877/edit
#https://medium.com/@nutanbhogendrasharma/classify-images-of-clothing-with-tensorflow-af3c80de1543#:~:text=Classify%20Images%20of%20Clothing%20With%20TensorFlow%201%20Import,...%208%20Train%20the%20model%20...%20More%20items


from __future__ import print_function
import binascii
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
from rembg import remove
from PIL import Image
import torch
from torch import nn
import torch.nn.functional as F
import torchvision
from torchvision import datasets, transforms
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np


  

def main_colour_in_image():
    NUM_CLUSTERS = 5
    remove_background()
    im = Image.open('new_img.png')
    im = im.resize((150, 150))      
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)


    vecs, dist = scipy.cluster.vq.vq(ar, codes)         
    counts, bins = np.histogram(vecs, len(codes))    

    index_max = np.argmax(counts)                    
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    print('most frequent is %s (#%s)' % (peak, colour))


def remove_background(): #https://www.geeksforgeeks.org/how-to-remove-the-background-from-an-image-using-python/
    input_path =  'static/images/sample.jpg'
    output_path = 'new_img.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

def image_classification():
    pass
