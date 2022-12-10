from tkinter import *
import cv2
import customtkinter


win= customtkinter.CTk()
customtkinter.set_appearance_mode("drak")
win.title('ทุกระบบจบที่บัง')
win.option_add("*Font", "Helvetica")
win.geometry("1000x550")
lbl1=customtkinter.CTkLabel(win, text='Number Of Rows                         :').place(x=100, y=35)
lbl2=customtkinter.CTkLabel(win, text='Number Of People Per Rows    :').place(x=100, y=75)
lbl3=customtkinter.CTkLabel(win, text='Photo To Be Taken                     :').place(x=100, y=155)

t1=customtkinter.CTkEntry(win, placeholder_text="number")
t2=customtkinter.CTkEntry(win, placeholder_text="number")
t3=customtkinter.CTkEntry(win, placeholder_text="result")
t1.place(x=350, y=35)
t2.place(x=350, y=75)
t3.place(x=350, y=155)

def add():
    ans = (int(t1.get()))*(int(t2.get()))
    print(ans)
    t3.insert(END, str(ans))
    
def takephoto():
    window = customtkinter.CTk()
    customtkinter.set_appearance_mode("drak")
    window.title("TAKE PHOTOS")
    vid = cv2.VideoCapture(1)
    
    canvas = Canvas(window, width = 1000, height = 550)
    canvas.pack()
    
    def open_camera():
        ok = True
        print("camera opened => Recording")

    btn_start= customtkinter.CTkButton(window, text='START', command = open_camera)
    btn_start.pack(side=LEFT)

    btn_quit= customtkinter.CTkButton (window, text='STOP', command = quit)
    btn_quit.pack(side=LEFT)

    window.mainloop()
customtkinter.CTkButton(win, text='Take Photo', width=150, command=takephoto).place(x=650, y=100)
customtkinter.CTkButton(win, text='Enter', width=100, command=add).place(x=200, y=120)
win.mainloop()
