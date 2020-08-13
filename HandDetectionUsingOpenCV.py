import cv2 as cv
import numpy as np

#creating an object for cammera
capture_img = cv.VideoCapture(0)

#infinite loop for gathering the image
while (True):
    #ret is the numpy array or pixels
    ret,frame = capture_img.read()
    #Converting the image into gray scale
    #vid_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    #Definnf ROI
    roi = frame[100:300,100:300]
    
    cv.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    
    vid_hsv= cv.cvtColor(roi,cv.COLOR_BGR2HSV)
    #vid_hsv= cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    #Anything of skin colour will be taken as 1 or white
    #Anything of not of skin colour will be taken as 0 or black
    
    lower_blue = np.array([0, 50 , 0])
    upper_blue = np.array([20, 255, 255])
    mask = cv.inRange(vid_hsv,lower_blue,upper_blue)
    
    #mask = cv.dilate(mask,kernel,iterations = 4)
    
    mask = cv.GaussianBlur(mask,(5,5),100)
    
    cv.imshow('HSV IMG',mask)
    
    
    contours,_ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    #cv.drawContours(roi,contours,-1,(0,255,0),3)
    
    cnt_max = max(contours, key= lambda x : cv.contourArea(x))
    cv.drawContours(roi,cnt_max,-1,(0,255,0),3)
    #hand_hull = cv.convexHull(cnt_max)
    
    #showing the captured image
    cv.imshow('Hand Detection',frame)
    #need to know the functgion of wait key here
    #cv.waitKey(100)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture_img.release()
cv.destroyAllWindows()
