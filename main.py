from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from collections import Counter
import os

#function for thresholding if needed
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

#function for creating the database file (.txt)
def createDataSheet():
    #this is to create the dataSheet 
    #once the dataSheet is created this function is not required any more
    dataSheet = open(currentDir + "dataSheet.txt", "a")
    actualNumbers = range(0,10) # 0 to 9
    numberVersions = range(1,10) # 1 to 9

    for number in actualNumbers:
        for version in numberVersions:
            fileName = currentDir + "images/numbers/" + str(number) + "." + str(version) + ".png"
            #print(fileName)
            currImg = Image.open(fileName)
            currImgArr = np.array(currImg)
            #getting the whole image array as a string of list to write in file
            currImgArrList = str(currImgArr.tolist())
            #wrtie in file
            line = str(number) + "::" + currImgArrList + "\n"
            dataSheet.write(line)


#function for recognition
#this is not that fancy. It just compares the pixel values of dataSheet and the given image
def identifyNum(filePath):
    matchedArr = [] #a list for storing matches
    file = open(currentDir + "dataSheet.txt", "r")
    data = file.read()
    data = data.split("\n")

    #getting the image array of the given image as a list
    givenImage = Image.open(filePath)
    imgArr = np.array(givenImage)
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
    #print(matching)

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
    plt.ylim(400)

    xloc = plt.MaxNLocator(11)
    plot2.xaxis.set_major_locator(xloc)

    plt.show()


currentDir = os.getcwd() + "/Digit_Recognition/"
#createDataSheet() #data sheet has been created so we don't need this any more

#open the test.png image in the same directory
testImagePath = currentDir + "/" + "test.png"
identifyNum(testImagePath)

