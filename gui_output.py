from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("light")
table = customtkinter.CTk()
table.title("ทุกระบบจบที่บัง")
table.geometry("1000x550")

inp_row, inp_column = 4, 14
total = 0
f1,f2 = Frame(table), Frame(table)
f1.grid(row=0, column=0, rowspan=2)
f2.grid(row=2, column=0)
Label(f1, text="Classroom", width=110, bg="#CBAACB").pack(padx=1, pady=10)
ans = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
for i in range(inp_row):
    for j in range(inp_column):
        if total > len(ans)-1:
            Button(f2, text="").grid(row=i, column=j)
        else:
            Button(f2, text=ans[total]).grid(row=i, column=j)
            total += 1

table.mainloop()