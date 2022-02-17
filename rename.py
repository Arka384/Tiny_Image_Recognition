from PIL import Image
import os

currentDir = os.getcwd() + "/Digit_Recognition/"



for i in range(0,10):
    folderPath = currentDir + "images/Fnt/Sample" + str(i) + "/"
    for j in range(1,250):
        oldFile = folderPath + "img_" + str(i) + "_ (" + str(j) + ").png"
        newFile = folderPath + "img_" + str(i) + "_" + str(j) + ".png"
        os.rename(oldFile, newFile)