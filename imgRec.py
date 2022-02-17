from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from collections import Counter
import os


def threshold(imgArray):
    balanceArr = []
    arr = imgArray

    for row in arr:
        for pixel in row:
            avgPixelVal = mean(pixel[:3])
            balanceArr.append(avgPixelVal)
    
    balance = mean(balanceArr)
    for row in arr:
        for pixel in row:
            if mean(pixel[:3]) > balance:
                pixel[0] = 255
                pixel[1] = 255
                pixel[2] = 255
                pixel[3] = 255
            else:
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
                pixel[3] = 255
    
    return arr



def identifyNum(filePath):
    matchedArr = [] #a list for storing matches
    file = open(currentDir + "newDataSheet.txt", "r")
    data = file.read()
    data = data.split("\n")

    #getting the image array of the given image as a list
    givenImage = Image.open(filePath)
    imgArr = np.array(givenImage)
    #imgArr = threshold(imgArr)
    imgArrList = imgArr.tolist()
    inQuestion = str(imgArrList)

    #now we will compare the pixel values
    for eachData in data:
        try:
            subArr = eachData.split("::")
            curNumber = subArr[0]
            curArr = subArr[1]

            #get each pixel from given image arr and data arr
            pixelInQuestion = inQuestion.split('],')
            pixelInData = curArr.split('],')

            x = 0
            while x < len(pixelInData):
                if(pixelInData[x] == pixelInQuestion[x]):
                    matchedArr.append(int(curNumber))
                x += 1
        
        except Exception as e:
            print(str(e))

    #print(matchedArr)
    matching = Counter(matchedArr)
    print(matching)

    """
    #plot the image given and the results 
    graphX = []
    graphY = []
    #creating x and y axix
    for elem in matching:
        graphX.append(elem)
        graphY.append(matching[elem])

    figure = plt.figure()
    plot1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    plot2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)

    plot1.imshow(imgArr)
    plot2.bar(graphX, graphY)
    plt.ylim(500)

    xloc = plt.MaxNLocator(11)
    plot2.xaxis.set_major_locator(xloc)

    plt.show()
    """

#################################################
#################################################

currentDir = os.getcwd() + "/Digit_Recognition/"
#print(currentDir)
#createDataSheet() #data sheet has been created so we don't need this any more

#open the test.png image in the same directory
testImagePath = currentDir + "/" + "6.png"
identifyNum(testImagePath)

"""
testImagePath = currentDir + "/" + "img_7_60.png"
identifyNum(testImagePath)
testImagePath = currentDir + "/" + "img_7_110.png"
identifyNum(testImagePath)
testImagePath = currentDir + "/" + "img_7_154.png"
identifyNum(testImagePath)
testImagePath = currentDir + "/" + "img_7_225.png"
identifyNum(testImagePath)
"""