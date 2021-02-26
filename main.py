# For making a custom haarcascade using your webcam for images to training the model

import cv2    # importing the opencv module
import os
import time

path = 'data/images'  # This will be the path where your images will be saved If you use the rasberry pi then it will be '/home/pi/desktop/data/images'
cameraBrightness = 190
moduleVal = 10 # This means that every (10th) frame will be saved

minBlur = 500 # This is the threshold which must be set for brightness

grayImage = False # Images will be saved as coloured for grey make it TRUE
saveData = True #This will save the data flag
showImage = True #It will display the image flag

imgWidth = 180  # Setting the image width and height
imgHeight = 120

global countFolder
cap = cv2.VideoCapture (0)  # if more than one camera or external camera then specify the number before
cap.set(3,640)
cap.set(4,480)
cap.set(10, cameraBrightness)

count = 0  # initializing the count number
countSave = 0 #Initializing the no of images

def saveDataFunc():   # User defined function
    global countFolder
    countFolder = 0 # initializing the folder count of images the number of times the program is run
    while os.path.exists(path + str(countFolder)):  # Using a while loop and increasing the countFolder each time
        countFolder = countFolder + 1
    os.makedirs(path + str(countFolder))    #Creating directory recursively

if saveData : saveDataFunc()

while True:    # Using a while loop for catching different frames
    success,img = cap.read()
    img = cv2.resize(img,(imgWidth,imgHeight))
    if grayImage : img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)  #Make it true above for gray image then this will automatically run
    if saveData:
        blur = cv2.Laplacian(img,cv2.cv_64F).var()  #For blur detection in image
        if count % moduleVal == 0 and blur > minBlur:  # Applying condition for minblur threshold and count divide by module val is 0
            nowTime = time.time()
            cv2.imwrite(path + str(countFolder)+'/' + str(countSave) + " " +str(int(blur))+" "+str(nowTime)+".png",img)  # This will be the name of image saved in the folder + the extension of image
            countSave += 1
        count+= 1 #Increasing the count
    if showImage:
        cv2.imshow("image",img) # for output as name image
    if cv2.waitkey(1) & 0xFF == ord('q'): # Setting key for closing the program
        break

cap.release()
cv2.destroyAllWindows()