import numpy as np
import cv2
img = np.full((400,400,3),255,np.uint8)


#line
pt1 = (50,100)
pt2 = (img.shape[0]-50,100)
pt3 = (img.shape[0]-50,300)
pt4 = (200,300)
lineColor = (0,0,255)
thick=3
lineType = cv2.LINE_AA
lineColor2 = (255,0,0)
#(x1,y1) (x2,y2)
#cv2.rectangle(img,pt1,pt4,lineColor,thick)
# x,y,w,h
#cv2.rectangle(img,(50,100,100,100),lineColor2,thick,lineType)
cv2.circle(img,(int(img.shape[0]/2),int(img.shape[1]/2)),100,(0,255,0),2,cv2.LINE_AA)

#text = "Hello OpenCV!"
# font = cv2.FONT_HERSHEY_SIMPLEX
# fontSize=1
# BlueColor = (255,0,0)
# thick = 1
# lineType = cv2.LINE_AA
#cv2.putText(img,text,(50,350),font,fontSize,BlueColor,thick,lineType)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()