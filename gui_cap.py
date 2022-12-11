from tkinter import *
import cv2 
from PIL import Image, ImageTk 
import customtkinter
from tkinter.ttk import *

app = customtkinter.CTk() 
customtkinter.set_appearance_mode("drak")
app.title("TAKE PHOTOS")
app.geometry("1000x550")

label_widget = Label(app)
label_widget.place(width = 1250, height = 650)

vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 650)

def open_camera():
    btn_open.after(1000, btn_open.destroy)
    _, frame = vid.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(opencv_image) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    label_widget.photo_image = photo_image 

    label_widget.configure(image=photo_image) 
    label_widget.after(10, open_camera)
    def start():
        cv2.imwrite("photo.png", frame)
        cv2.destroyWindow()

    return customtkinter.CTkButton(app, text='START', command = start).pack(side=LEFT,anchor=S)
btn_quit = customtkinter.CTkButton(app, text='STOP', command = quit)
btn_quit.pack(side=LEFT, anchor=SW)
btn_open = customtkinter.CTkButton(app, text="Open Camera", command = open_camera)
btn_open.pack(side=RIGHT, anchor=SE)

app.mainloop()