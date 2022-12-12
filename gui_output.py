from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("lilght")
table = customtkinter.CTk()
table.title("ทุกระบบจบที่บัง")
table.geometry("1000x550")

inp_row, inp_column = 7, 4
f1,f2 = Frame(table), Frame(table)
f1.grid(row=0, column=0, rowspan=2)
f2.grid(row=2, column=0)
Label(f1, text="Classroom", width=25, bg="#CBAACB").pack(padx=385, pady=10)
ans = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22"]
# for x in ans:
for x in ans:
    Button(f2, text=x).grid(padx=5, pady=5)

table.mainloop()