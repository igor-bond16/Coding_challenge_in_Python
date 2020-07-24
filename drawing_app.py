import cv2
import numpy as np

drawing = False 
color = (255,255,255)
ix,iy = 0,0

def nothing(x):
    pass

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,color

    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    s = cv2.getTrackbarPos('Size','image')
    i = cv2.getTrackbarPos(switch,'image')

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if i == 1:
            b,g,r = 0,0,0
        if drawing == True:
            cv2.circle(img,(x,y),s,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        if i == 1:
            b,g,r = 0,0,0
        drawing = False
        cv2.circle(img,(x,y),s,(b,g,r),-1)

q
img = np.full((800,800,3),255,np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('Size', 'image',1,30,nothing)
cv2.setMouseCallback('image',draw_circle)
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while True:  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('image',img)
cv2.destroyAllWindows()
