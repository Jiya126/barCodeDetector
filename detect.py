import imp
from re import T
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    s, img = cap.read()

    for code in decode(img):
        data = code.data.decode('utf-8')
        print(data)
        pts = np.array([code.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        pts2 = code.rect
        cv2.polylines(img, [pts], True, (0,255,0), 4)
        cv2.putText(img, data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

    cv2.imshow('detector', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()