### README FILE

Hey!! **_It's a super easy method by which you can train your own model for any object you want and use that trained model on live video/downloaded video and image using opencv_**

## STEPS TO FOLLOW
1- Use the **'main.py'** file and run in on your pyhton IDE for fetching the images using your web-cam 
(Note - You can also use any other device to capture the images manually)

2- Run the program two times for obtaining positive and negative images                       
- **Positive** - The actual images of the object 
- **Negative** - Images of object similar to the original object or related to it yet false images( Example- For a car model the negative images can be road,traffic signal or anything 
like that which might come in the detecing videos)

(Note - Always use 2 to 3 times more negative images than the positive images)

The images will be saved and more the number of images from different angles more will be the accuracy

---
3- Now for the implementation part use [This website](https://amin-ahmadi.com/cascade-trainer-gui/)
Upload the positive and negative images in the trainer GUI and tell the **negative image count** and in **common** set the **No. of stages** as 17 and in **Cascade** the **Sample width** as 38 
Then press the **START** button

4- Download the xml file of the model obtained and then open the **'Using Trained Model.py'** and replace the name in the required place and test the modelon any video,image or live video

## NOTE- RASBERRY PI CAN ALSO BE INTEGRTED IN THIS

Contact me on - [Linekdin](https://www.linkedin.com/in/sajeev-singh-983b721bb/)

