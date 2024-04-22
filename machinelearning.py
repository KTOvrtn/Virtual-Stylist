#https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
#https://www.tensorflow.org/tutorials/keras/classification#use_the_trained_model
#https://towardsdatascience.com/fashion-mnist-classification-with-tensorflow-featuring-deepmind-sonnet-aeb3987d826e
#https://www.kaggle.com/code/scratchpad/notebook6d15019877/edit
#https://medium.com/@nutanbhogendrasharma/classify-images-of-clothing-with-tensorflow-af3c80de1543#:~:text=Classify%20Images%20of%20Clothing%20With%20TensorFlow%201%20Import,...%208%20Train%20the%20model%20...%20More%20items


from __future__ import print_function
import binascii
import PIL.Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
from rembg import remove
import numpy as np
import os

def main_colour_in_image(image):
    NUM_CLUSTERS = 5
    img = PIL.Image.open(image)
    frac = 0.5

    left = img.size[0]*((1-frac)/2)
    upper = img.size[1]*((1-frac)/2)
    right = img.size[0]-((1-frac)/2)*img.size[0]
    bottom = img.size[1]-((1-frac)/2)*img.size[1]
    cropped_img = img.crop((left, upper, right, bottom))

    im = cropped_img.resize((300,300))      
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)


    vecs, dist = scipy.cluster.vq.vq(ar, codes)         
    counts, bins = np.histogram(vecs, len(codes))    

    index_max = np.argmax(counts)                    
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    valuecheck = 0
    while colour == "defc00" or colour == "ddfb00" or colour == "defb01":
        try:
            index_max = np.argsort(counts)[-valuecheck]
            peak = codes[index_max]
            colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
            valuecheck += 1
        except IndexError:
            color = "defc00"
            break

    if len(colour) != 6:
        colour = colour[:6]
    return colour

def remove_background(image, number): #https://www.geeksforgeeks.org/how-to-remove-the-background-from-an-image-using-python/
    input = PIL.Image.open(image)
    output = remove(input)
    output.save("static/uploaded_images/temporaryimages/imagewithoutbg.png")
    output.save(f"static/uploaded_images/{number+1}.png")

def combine_images():
    # https://www.codespeedy.com/merge-two-images-in-python/
    # https://www.bing.com/search?pglt=41&q=how+to+combine+two+images+in+python&cvid=382a44a6da6e42049e0f637c73ab3c9a&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIECAEQADIECAIQADIECAMQADIECAQQADIECAUQADIECAYQADIECAcQADIECAgQANIBCTI4NzU0ajBqMagCALACAA&FORM=ANNTA1&PC=LCTS
    background = PIL.Image.open('static/images/colour_comparison.jpg')
    foreground = PIL.Image.open("static/uploaded_images/temporaryimages/imagewithoutbg.png")
    dimensions = (2880, 1800)
    newImage = foreground.resize(dimensions)
    background.paste(newImage, (0, 0), newImage)
    background.save("static/uploaded_images/temporaryimages/mergedimage.png")