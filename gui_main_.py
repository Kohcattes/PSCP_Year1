from tkinter import *
import cv2
import customtkinter
from PIL import Image, ImageTk 
from tkinter.ttk import *

root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
root.title("ทุกระบบจบที่บัง")
root.geometry('1000x550')

lbl1=customtkinter.CTkLabel(root, text="Welcome to", font=('clearlyu pua', 40)).pack(padx=10, pady=10)
lbl2=customtkinter.CTkLabel(root, text='" ทุกระบบจบที่บัง! "', font=('fixed', 30)).pack(padx=10, pady=10)
lbl4=customtkinter.CTkLabel(root, text="|", font=('Helvetica', 30)).pack()
lbl5=customtkinter.CTkLabel(root, text="|", font=('Helvetica', 30)).pack()
lbl6=customtkinter.CTkLabel(root, text="\/", font=('Helvetica', 30)).pack()

def win():
    win = customtkinter.CTk()
    customtkinter.set_appearance_mode("drak")
    win.title('ทุกระบบจบที่บัง')
    win.option_add("*Font", "Helvetica")
    win.geometry("1000x550")
    lbl1=customtkinter.CTkLabel(win, text='Number Of Rows                         :').place(x=100, y=35)
    lbl2=customtkinter.CTkLabel(win, text='Number Of People Per Rows     :').place(x=100, y=75)

    t1=customtkinter.CTkEntry(win, placeholder_text="number")
    t2=customtkinter.CTkEntry(win, placeholder_text="number")
    t1.place(x=350, y=35)
    t2.place(x=350, y=75)

    def photo():
        app = customtkinter.CTk() 
        customtkinter.set_appearance_mode("drak")
        app.title("TAKE PHOTOS")
        app.geometry("1000x550")
        
        #สร้างกล่องใส่วิดีโอ
        label_widget = Label(app)
        label_widget.place(width = 1250, height = 650)

        #ตั้งค่าขนาดวิดีโอที่จะแสดงบน tk()
        vid = cv2.VideoCapture(0)
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1300)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 650)

        dic_pic = dict() #สรุปตอนนี้ให้dictเก็บค่าตำแหน่งyไว้เพื่อดึงมาใช้ในการคำนวนต่อไปให้เร็วขึ้น
        face_track = cv2.CascadeClassifier('face_alt.xml') #เพิ่มส่วนของการหาตำแหน่ง

        #ฟังค์ชั่นเปิดกล้อง
        def open_camera():
            _, frame = vid.read()
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image) 
            photo_image = ImageTk.PhotoImage(image=captured_image) 
            label_widget.photo_image = photo_image 

            label_widget.configure(image=photo_image) 
            label_widget.after(10, open_camera)

        #ฟังค์ชั่นการทำงานของโปรเเกรมจับใบหน้า
        def start():
            _, frame = vid.read()
            cv2.imwrite("student%02d.png" %len(dic_pic), frame)#กดถ่ายช็อตนึงแล้วเอามาทำงานหาหน้าคนเลย
            img = cv2.imread("student%02d.png" %len(dic_pic))
            gray_scal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            y = (face_track.detectMultiScale(gray_scal))[0][1]
            dic_pic["student%02d.png" %len(dic_pic)] = y
            
        def seat():
            customtkinter.set_appearance_mode("light")
            table = customtkinter.CTk()
            table.title("ทุกระบบจบที่บัง")
            table.geometry("1000x550")
            
            
            chair = tuple(sorted(dic_pic.items(), key=lambda x:x[1]))
            
            row = int(t1.get()) 
            column = int(t2.get())
            
            total = 0
            f1,f2 = Frame(table), Frame(table)
            f1.grid(row=0, column=0, rowspan=2)
            f2.grid(row=2, column=0)
            
            customtkinter.CTkButton(f1, text='PROJECTOR', width=999).pack(padx=1, pady=10)
            
            for i in range(row):
                for j in range(column):
                    if total > len(chair)-1:
                        customtkinter.CTkButton(f2, text="", width=50).grid(row=i, column=j)
                    else:
                        customtkinter.CTkButton(f2, text=chair[total], width=50).grid(row=i, column=j)
                        total += 1
            btn3 = customtkinter.CTkButton(table, text='FINISH', width=100, command=quit)
            btn3.place(x=470, y=500)
            table.mainloop()
                
        btn_quit = customtkinter.CTkButton(app, text='STOP', command = seat)
        btn_quit.pack(side=RIGHT, anchor=SE)
        btn_start = customtkinter.CTkButton(app, text='CAPTURE', command = start)
        btn_start.pack(side=LEFT, anchor=SW)

        open_camera()
        app.mainloop()
        
    def add():
        row = int(t1.get()) 
        column = int(t2.get())
        print(row, column)
        btn2.after(100, btn2.destroy)
        return customtkinter.CTkButton(win, text='Take Photo', width=150, command=photo).place(x=650, y=100)
    
    btn2 = customtkinter.CTkButton(win, text='Enter', width=150, command=add)
    btn2.place(x=650, y=100)

    win.mainloop()
button = customtkinter.CTkButton(master=root, text="Start!", command=win)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()