'''full'''
import cv2
from tkinter import *

cam_port = 0
cam = cv2.VideoCapture(0)
dic_pic = dict()
body_model = cv2.CascadeClassifier('body_detec.xml')
img = cv2.imread('photo1,jpg')
gray_scal = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
human = body_model.detectMultiScale(gray_scal)




face_track = cv2.CascadeClassifier('face_alt.xml')

def opencamera():
    total = 1
    while True:
        result, image = cam.read()
        cv2.imshow("input student len", image)
        if cv2.waitKey(1) & 0x0FF == ord("q"):
            cv2.imwrite("photo%02d.png" %total, image)#กดถ่ายช็อตนึงแล้วเอามาทำงานหาหน้าคนเลย
            img = cv2.imread("photo%02d.png" %total)#ไม่มั่นใจว่าเราจะเสียเวลาขั้นตอนนี้หรือป่าว
            gray_scal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            y = (face_track.detectMultiScale(gray_scal))[0][1]#ต้องได้แค่หน้าเดียวไม่งั้นได้ตำแหน่งผิดแน่หรือถ้าไม่ได้ตำแหน่งมาก็แตก
            dic_pic['photo%02d.png'%total] = y
            total += 1
        if cv2.waitKey(1) & 0x0FF == ord("d"):
            break
    chair = tuple(sorted(dic_pic.items(), key=lambda x:x[1]))
    return chair
#ส่วนของgui
base = Tk()
base.title("โปรแกรมหาที่นั้่ง")
#end gui


#ได้รูปนักศึกษามาแล้วต่อไปเป็นส่วนของการจัดเรียง



#finish sort .next, ui output design



#end program
