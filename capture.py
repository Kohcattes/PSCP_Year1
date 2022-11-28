import cv2  
cam_port = 0
cam = cv2.VideoCapture(0)
total = 1
while True:
    result, image = cam.read()
    cv2.imshow("photo", image)
    if cv2.waitKey(1) & 0x0FF == ord("q"):
        cv2.imwrite("photo%d.png" %total, image)
        total += 1
    if cv2.waitKey(1) & 0x0FF == ord("d"):
        break
cv2.destroyWindow()
