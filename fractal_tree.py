import cv2
import math
import numpy as np

def nothing(x):
    pass

def drawTree(a, b, pos, deepness,angle,img):
    if deepness:
        c = a + int(math.cos(math.radians(pos)) * deepness * 10.0)
        d = b + int(math.sin(math.radians(pos)) * deepness * 10.0)
        cv2.line(img,(a, b), (c, d),(255,255,255),1)
        drawTree(c, d, pos - angle, deepness - 1,angle,img)
        drawTree(c, d, pos + angle, deepness- 1,angle,img)

def draw(event,x,y,flags,param):
    global img
    img = np.zeros((800,800,3),np.uint8)
    b = cv2.getTrackbarPos('bar','image')
    drawTree(370, 650, -90,10,angle=b,img=img)

img = np.zeros((800,800,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('bar','image',0,360,nothing)
cv2.setMouseCallback('image',draw)

while True: 
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    cv2.imshow('image',img)
cv2.destroyAllWindows()