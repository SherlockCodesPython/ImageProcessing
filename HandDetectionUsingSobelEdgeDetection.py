import skimage 
from skimage.filters import sobel
import cv2 as cv
import numpy as np

vid_cap = cv.VideoCapture(0)

while (True):
    ret,frame = vid_cap.read()
    
    cnvt_vdo_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #cnvt_vdo_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    roi = cnvt_vdo_gray[100:300,100:300]
    #roi = cnvt_vdo_hsv[100:300,100:300]
    cv.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'Put your Hand In The box',(0,50),font,1,(0,0,255),3, cv.LINE_AA)
    #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    
    #lower_blue = np.array([0, 50 , 0])
    #upper_blue = np.array([20, 255, 255])
    #mask = cv.inRange(cnvt_vdo_gray,lower_blue,upper_blue)
    #mask = cv.dilate(mask,kernel,iterations = 4)
    #mask = cv.GaussianBlur(mask,(5,5),100)
    #cv.imshow('HSV IMG',mask)
    #vid_sobel = sobel(mask)
    
    vid_sobel = sobel(roi)
    
    cv.imshow("Sobel", vid_sobel)
    
    cv.imshow("Normal Video Capture", frame)
    
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
vid_cap.release()
cv.destroyAllWindows()
    
    
