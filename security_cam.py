import cv2
from datetime import datetime
import requests
import time

token = 'Your Token'

cap = cv2.VideoCapture(0)
lastframe = None

def send_msg():
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization':'Bearer '+token}
    data = {"message":"Someone in your room."}
    image = '/home/igor-bond/image.jpg'
    file = {'imageFile': open(image, 'rb')}
    r = requests.post(url, headers=headers, params=data, files=file,)
    
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        if lastframe is None:
            lastframe = gray.astype("float")
        
        cv2.accumulateWeighted(gray,lastframe,0.6)
        frame_diff = cv2.absdiff(gray,cv2.convertScaleAbs(lastframe))
        thresh = cv2.threshold(frame_diff,3,255,cv2.THRESH_BINARY)[1]
        contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) > 30:
                time.sleep(0.2)
                now = datetime.now()
                img = cv2.resize(frame,(int(frame.shape[1]*0.5),int(frame.shape[0]*0.5)))
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,f'{now}',(100,350),font,1,(0,0,255),4,cv2.LINE_AA)
                cv2.imwrite('/home/igor-bond/image.jpg',img)
                send_msg()
                lastframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY).astype("float")
                break

        cv2.imshow('frame',frame)  
           
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()
