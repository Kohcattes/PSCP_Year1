from tkinter import *
import cv2  

win=Tk()
win.title('Hello Python')
win.option_add("*Font", "Helvetica")
win.geometry("1000x550")
lbl1=Label(win, text='Number Of Rows                         :').place(x=100, y=50)
lbl2=Label(win, text='Number Of People Per Rows    :').place(x=100, y=100)
lbl3=Label(win, text='Photo To Be Taken                     :').place(x=100, y=200)
Button(win, text='Take Photo', width=20, bd=3, command=win.quit).place(x=650, y=100)

t1=Entry(win, bd=3)
t2=Entry(win, bd=3)
t3=Entry(bd=4)
t1.place(x=350, y=50)
t2.place(x=350, y=100)
t3.place(x=350, y=200)

def add():
    print(t1.get())
    print(t2.get())
    ans = (int(t1.get()))*(int(t2.get()))
    t3.insert(END, str(ans))
    
# def takephoto():
    #ใส่ฟังค์ชั่นcapture
    
    
Button(win, text='Enter', width=20, bd=1, command=add).place(x=200, y=150)
win.mainloop()