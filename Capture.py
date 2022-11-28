import cv2  
cam_port = 0
cam = cv2.VideoCapture(0)
total, dic_pic = 1, dict()
while True:
    result, image = cam.read()
    cv2.imshow("photo", image)
    if cv2.waitKey(1) & 0x0FF == ord("q"):
        cv2.imwrite("photo%d.png" %total, image)
        dic_pic['photo'+str(total)+'.png'] = total
        total += 1
    if cv2.waitKey(1) & 0x0FF == ord("d"):
        break
print(dic_pic)
cv2.destroyWindow()
