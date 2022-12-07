import cv2

cam_port = 0
cam = cv2.VideoCapture(0)
total, dic_pic = 1, dict()
#เพิ่มส่วนของการหาตำแหน่ง

#end of position
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
cv2.destroyWindow()#สักคนแก้ตรงนี้ดิ้ไม่ให้มันError ตอนปิดหน้าต่าง เอมแก้ให้หน่อย
#ได้รูปนักศึกษามาแล้วต่อไปเป็นส่วนของการจัดเรียง

#finish sort .next, ui output design
# ดราฟตรงนี้ฝากออกแบบ ui หน่อยว่าจะแสดงเป็นรูปแบบไหน เอาแบบดุดัน ฟอดเรนเจอร์
#end program
body_model = cv2.CascadeClassifier('body_detec.xml')#ใครก็ได้มาเปลี่ยนไอ้แท็คร่างกายให้เป็นแท็คหน้าดิ้ ออมก็ได้
img = cv2.imread('photo1.jpg') #รูปภาพ
gray_scal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #save
human = body_model.detectMultiScale(gray_scal) #save
print(human) # keep to show
for x, y, w, h in human:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2) #แก้ไงดีวะกลัวว่ามันจะแท็ค หลายจุดแล้วloopแตก
cv2.imshow('Aom', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
