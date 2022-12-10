from tkinter import *
import cv2  
import customtkinter

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
    customtkinter.set_appearance_mode("dark")
    win.title('ทุกระบบจบที่บัง')
    win.option_add("*Font", "Helvetica")
    win.geometry("1000x550")
    lbl1=customtkinter.CTkLabel(win, text='Number Of Rows                         :').place(x=100, y=35)
    lbl2=customtkinter.CTkLabel(win, text='Number Of People Per Rows      :').place(x=100, y=75)
    lbl3=customtkinter.CTkLabel(win, text='classroom seat                            :').place(x=100, y=155)

    t1=customtkinter.CTkEntry(win, placeholder_text="number")
    t2=customtkinter.CTkEntry(win, placeholder_text="number")
    t3=customtkinter.CTkEntry(win, placeholder_text="result")
    t1.place(x=350, y=35)
    t2.place(x=350, y=75)
    t3.place(x=350, y=155)

    def add():
        print(t1.get())
        print(t2.get())
        ans = (int(t1.get()))*(int(t2.get()))
        t3.insert(END, str(ans))
        
    def takephoto():
        cam = cv2.VideoCapture(0)
        total = 1
        while True:
            result, image = cam.read()
            cv2.imshow("photo", image)
            if cv2.waitKey(1) & 0x0FF == ord("q"):
                cv2.imwrite("photo%d.png" %total, image)
                total += 1
            if cv2.waitKey(1) & 0x0FF == ord("d"):
                break
        cv2.destroyWindow()
        
    customtkinter.CTkButton(win, text='Take Photo', width=150, command=takephoto).place(x=650, y=100)
    customtkinter.CTkButton(win, text='Enter', width=100, command=add).place(x=200, y=120)
    win.mainloop()

button = customtkinter.CTkButton(master=root, text="Start!", command=win)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
root.destroy
root.mainloop()