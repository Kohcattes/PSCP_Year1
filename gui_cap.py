from tkinter import *
import cv2 
from PIL import Image, ImageTk 
import customtkinter
from tkinter.ttk import *

app = customtkinter.CTk() 
customtkinter.set_appearance_mode("drak")
app.title("TAKE PHOTOS")
app.geometry("1000x550")

#สร้างกล่องใส่วิดีโอ
label_widget = Label(app)
label_widget.place(width = 1250, height = 650)

#ตั้งค่าขนาดวิดีโอที่จะแสดงบน tk()
vid = cv2.VideoCapture(1)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1300)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 650)

lis = []
dic_pic = dict() #สรุปตอนนี้ให้dictเก็บค่าตำแหน่งyไว้เพื่อดึงมาใช้ในการคำนวนต่อไปให้เร็วขึ้น
face_track = cv2.CascadeClassifier('face_alt.xml') #เพิ่มส่วนของการหาตำแหน่ง

def open_camera():
    _, frame = vid.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(opencv_image) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    label_widget.photo_image = photo_image 

    label_widget.configure(image=photo_image) 
    label_widget.after(10, open_camera)
    
def start(i):
    _, frame = vid.read()
    cv2.imwrite("photo.png", frame)#กดถ่ายช็อตนึงแล้วเอามาทำงานหาหน้าคนเลย
    img = cv2.imread("photo%d.png" %i)#ไม่มั่นใจว่าเราจะเสียเวลาขั้นตอนนี้หรือป่าว
    gray_scal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    y = (face_track.detectMultiScale(gray_scal))[0][1]#ต้องได้แค่หน้าเดียวไม่งั้นได้ตำแหน่งผิดแน่หรือถ้าไม่ได้ตำแหน่งมาก็แตก
    dic_pic["photo%d.png" %i] = y
    chair = tuple(sorted(dic_pic.items(), key=lambda x:x[1]))
    lis.append(chair)
    print(lis)

btn_start = customtkinter.CTkButton(app, text='CAPTURE', command = start)
btn_start.pack(side=LEFT, anchor=SW)

btn_quit = customtkinter.CTkButton(app, text='STOP', command = quit)
btn_quit.pack(side=RIGHT, anchor=SE)

open_camera()
app.mainloop()
