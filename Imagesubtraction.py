# -*- coding: utf-8 -*-
#Created on Thu Mar 23 14:24:40 2023

#@author: CKW


import cv2 as cv
import numpy as np
import matplotlib as plt
import os



path=r'E:\Downloads\DataAE\Data\3_Immersion_Inhibited_delayed (60 s)\1_Pre-processed Images'
image0 = cv.imread(r'E:\Downloads\DataAE\Data\3_Immersion_Inhibited_delayed (60 s)\image0.tif', 1)
Images = os.listdir(path)



#image1 = os.path.join(path, Images[11])
#print(image1)
#image11 = cv.imread(image1, 0)
#subtract2 = cv.subtract(image11, image0)
#cv.imshow(image1, subtract2)
#cv.waitKey(0)
#cv.destroyAllWindows()




for i in Images:
    imgPath=os.path.join(path,i)
    #print(imgPath)
    #image0 = cv.imread('image0.tif', 1)
    image = cv.imread(imgPath, 1)
    subtract = cv.subtract(image0, image)
    cv.imwrite(f'E:\OutputImages\Immersion_inhibited_delayed\{i}.tif', subtract)
    
    
    #cv.imshow(imgPath,image)
    #cv.waitKey(10000)
#cv.destroyAllWindows()

#img = cv.imread(path,0)
#cv.imshow('image',img)
#cv.waitKey(10000)
#cv.destroyAllWindows() 