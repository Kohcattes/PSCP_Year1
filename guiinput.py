from tkinter import *
import customtkinter
from tkinter.ttk import *

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

def add():
    ans = (int(t1.get()))*(int(t2.get()))
    print(ans)
    btn2.after(100, btn2.destroy)
    return customtkinter.CTkButton(win, text='Take Photo', width=150, command=quit).place(x=650, y=100)
btn2 = customtkinter.CTkButton(win, text='Enter', width=100, command=add)
btn2.place(x=650, y=100)

win.mainloop()