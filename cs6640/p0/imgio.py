"""
cs6640 P0 (2022F))
Written by Yura Hwang
"""

import os 
import numpy as np 
import skimage as sk
import matplotlib.pyplot as plt 

DIR_SOURCE = r".\images\\" 
DIR_OUT = r".\out\\"

# IMAG IO--READ  
def img_read(DIR,FILENAME): 
    if not DIR: 
        raise NotADirectoryError
    return plt.imread(DIR + FILENAME)


# IMAGE IO--WRITE
def img_write(DIR,fig):    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    fig.savefig(DIR + 'output.png')


# IMAGE DISPLAY
def img_display(r,c): 
    fig.suptitle('Images in grid')
    for i in range(r): 
        for j in range(c): 
            ex = imgs_gray[r*i + j]   
            ax[i,j].imshow(ex, cmap = 'gray')   
    plt.show()


# MAIN 
if __name__ == "__main__": 
    img_list = os.listdir(DIR_SOURCE)
    imgs_input = []

    # Q2a: Read images 
    for img_name in img_list: 
        imgs_input.append(img_read(DIR_SOURCE,img_name))
        
    # Q2b: Convert the input imgs into grayscale 
    imgs_gray = []
    weights = [0.3, 0.6, 0.1] # From Q1.c  
    for img in imgs_input:
        # Grayscale input 
        g = 0
        if img.ndim == 2: 
            g = img 
        # Grayscale conversion 
        else: 
            g  = img[..., :3] * weights 
            g = g[...,0] + g[...,1] + g[...,2]
        imgs_gray.append(g)

    r = 2 
    c = 2 
    fig, ax = plt.subplots(r, c)    
    # Q2c: Display the imges in grid 
    img_display(r,c)
    # Q2d: Save plot 
    img_write(DIR_OUT,fig) 
  