import skimage 
import numpy as np
import cv2 as cv
from skimage.filters import roberts

capture_video = cv.VideoCapture(0)

while (True):
    
    ret,frame = capture_video.read()
    
    #roi = frame[100:300,100:300]
    #cv.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    
    vid_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #vid_gray = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    roi = vid_gray[100:300,100:300]
    cv.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    
    vid_roberts_edge = roberts(roi)
    
    cv.imshow("Normal Video", frame)
    
    cv.imshow("Roberts Edge Detection", vid_roberts_edge)
    
    #cv.waitKey(100)
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
capture_video.release()
cv.destroyAllWindows()



