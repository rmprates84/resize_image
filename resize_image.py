# This code resizes images to a size chosen by the user
# Copyright 2018 - Ricardo Prates

#Modules
from numpy import *
from tqdm import tqdm
from PIL import Image
import os
import matplotlib.pyplot as plt
from keras.preprocessing import image

#Paths
path = os.getcwd()
path_1 = path + '\\data'
path_2 = path + '\\data_resized'

#Listing image path
listing = os.listdir(path_1)

#Number of samples
num_samples = size(listing)
print('Number of samples',num_samples)

#Images dimensions - Insert the rows and columns
img_rows, img_cols, img_channels = 224, 224, 3

#Resize images in path 1 to path 2
for file in tqdm(listing):
    im = Image.open(path_1+'\\'+file)
    img = im.resize((img_rows,img_cols))
    img.save(path_2+'\\'+file)

#List path 2 and show a chosen image
imlist = os.listdir(path_2)
image_path = path_2+'\\'+imlist[30]
imagem_red = image.load_img(image_path)
plt.imshow(imagem_red)
plt.show()

