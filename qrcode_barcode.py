import pyqrcode
import barcode
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image
import cv2

#b = pyqrcode.QRCode('https://www.youtube.com/channel/UCDYbu9aViDvkubFcwgbbKDA',error='M')
#a = pyqrcode.create(content="Hello From Jetsonnano",error='H')
#a.png(file='test.png',scale=6)

#b.png('uca.png',scale=6)
#d = '938469387183'
#a = barcode.get_barcode_class('ean13')
#b = a(d,writer=ImageWriter())
#c = b.save('barcode')
#d = decode(Image.open('/home/igor-bond/uca.png'))
#e = decode(Image.open('/home/igor-bond/barcode.png'))

#print(d[0].data.decode("utf-8"))
#print(e[0].data.decode('utf-8'))
#cap = cv2.VideoCapture(0)
#font = cv2.FONT_HERSHEY_SIMPLEX
#while True:
#    ret,frame = cap.read()

#    d = decode(frame)
#    if d:
#        #print(d[0].data.decode('utf-8'))
#        frame = cv2.putText(frame,d[0].data.decode('ascii'),(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
#    cv2.imshow('frame',frame)#

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#cap.release()

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        d = decode(frame)
        if d:
            for barcode in d:
                x,y,w,h = barcode.rect
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                barcodeData = barcode.data.decode('utf-8')
                barcodeType = barcode.type
                text = f"{barcodeData} ({barcodeType})"
                frame = cv2.putText(frame,barcodeData,(x,y-10),font,.5,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

