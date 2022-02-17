from PIL import Image
import numpy as np
import os

def createDataSheet():
    #this is to create the dataSheet 
    #once the dataSheet is created this function is not required any more
    dataSheet = open(currentDir + "newDataSheet.txt", "a")
    actualNumbers = range(0,10) # 0 to 9
    numberVersions = range(1,250) # 1 to 249

    for number in actualNumbers:
        folderPath = currentDir + "images/Fnt/Sample" + str(number) + "/"
        for version in numberVersions:
            fileName =  folderPath + "img_" + str(number) + "_" + str(version) + ".png"
            #print(fileName)
            currImg = Image.open(fileName)
            currImgArr = np.array(currImg)
            #getting the whole image array as a string of list to write in file
            currImgArrList = str(currImgArr.tolist())
            #wrtie in file
            line = str(number) + "::" + currImgArrList + "\n"
            dataSheet.write(line)


currentDir = os.getcwd() + "/Digit_Recognition/"
createDataSheet()