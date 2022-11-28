import cv2  
#cam_port = 0
#cam = cv2.VideoCapture(0)
#total = 1
#while True:
#    result, image = cam.read()
#    cv2.imshow("photo", image)
#    if cv2.waitKey(1) & 0x0FF == ord("q"):
#        cv2.imwrite("photo%d.png" %total, image)
#        total += 1
#    if cv2.waitKey(1) & 0x0FF == ord("d"):
#        break
#cv2.destroyWindow()
body_model = cv2.CascadeClassifier('body_detec.xml')
#for i in range(1, total):
img = cv2.imread('photo1.jpg') #รูปภาพ
gray_scal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
human = body_model.detectMultiScale(gray_scal)
print(human)
for x, y, w, h in human:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
cv2.imshow('Aom', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
