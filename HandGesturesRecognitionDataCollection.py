import skimage 
from skimage.filters import sobel
import cv2 as cv
import numpy as np
import os

BASEDIR = (r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand")
CATEGORIES = ["0","1","2","3","4","5"]

for category in CATEGORIES:
    path = os.path.join(BASEDIR,category)

vid_cap = cv.VideoCapture(0)

while (True):
    ret,frame = vid_cap.read()
    
    cnvt_vdo_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cnvt_vdo_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    roi = cnvt_vdo_gray[100:300,100:300]
    #roi = cnvt_vdo_hsv[100:300,100:300]
    cv.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'Put your Hand In The box',(0,50),font,1,(0,0,255),3, cv.LINE_AA)
    #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    
    lower_skin = np.array([0,30,60])
    upper_skin = np.array([20,150,255])
    mask = cv.inRange(cnvt_vdo_hsv,lower_skin, upper_skin)
    mask = cv.GaussianBlur(mask,(5,15),1000)
    cv.imshow("HSV Image", mask)
    
    
    vid_sobel = sobel(roi)
    
    cv.imshow("Sobel", vid_sobel)
    
    cv.imshow("Normal Video Capture", frame)
    
    count = 0
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
        
    if cv.waitKey(100) & 0xFF == ord('0'):
        #Store the image in the path above
        #cv.imwrite(os.path.join(BASEDIR+""+"0", 'anik.png'), vid_sobel)
        cv.imwrite(os.path.join(r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand\0", 'anik.png'), roi)
        #count = count+1
    if cv.waitKey(100) & 0xFF == ord('1'):
        #store the image in the path above
        cv.imwrite(os.path.join(r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand\1", 'anik.png'), roi)
    if cv.waitKey(100) & 0xFF == ord('2'):
        #Store the image in the path above
        cv.imwrite(os.path.join(r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand\2", 'anik.png'), roi)
    if cv.waitKey(100) & 0xFF == ord('3'):
        #store the image in the path above
        cv.imwrite(os.path.join(r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand\3", 'anik.png'), roi)
    if cv.waitKey(100) & 0xFF == ord('4'):
        #Store the image in the path above
        cv.imwrite(os.path.join(r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand\4", 'anik.png'), roi)
    if cv.waitKey(100) & 0xFF == ord('5'):
        #store the image in the path above
        cv.imwrite(os.path.join(r"C:\Users\Anik Chatterjee\Untitled Folder\DataHand\5", 'anik.png'), roi)
        
    
vid_cap.release()
cv.destroyAllWindows()
    
    
