import cv2
import tkinter import *

cam_port = 0
cam = cv2.VideoCapture(0)
dic_pic = dict()
#เพิ่มส่วนของการหาตำแหน่ง
face_track = cv2.CscadeClassifier('face_alt.xml')
#end of position
def opencamera():
    total = 1
    while True:
        result, image = cam.read()
        cv2.imshow("input student len", image)
        if cv2.waitKey(1) & 0x0FF == ord("q"):
            cv2.imwrite("photo%02d.png" %total, image)
            img = cv2.imread("photo%02d.png" %total)
            gray_scal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            y = (face_track.detectMultiScale(gray_scal))[0][1]
            dic_pic['photo%02d.png'%total] = y
            total += 1
        if cv2.waitKey(1) & 0x0FF == ord("d"):
            break
    chair = tuple(sorted(dic_pic.items(), key=lambda x:x[1]))
    return chair
base = Tk()
base.title("โปรแกรมหาที่นั่ง")

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

