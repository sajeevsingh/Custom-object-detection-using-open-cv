# Once you have trained the model using the cascade trainger and providing all the positive and negative images then
# Use this for using the trained model

import cv2

print(cv2.__version__)

cascade_src = 'model.xml'  # This should be the model.xml file obtained from the cascade trainger and use the correct name here
video_src =  # for video source in which you want to try


cap = cv2.VideoCapture(video_src) # if try on live use 0 instead
model_cascade = cv2.CascadeClassifier(cascade_src) #Using the cascade classifier

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    model = model_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) # drawing rectangle on detected area

    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()