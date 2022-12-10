from tkinter import *
from tkinter import messagebox

root = Tk()
#root.option_add("*Font", "30")
root.title("ทุกระบบจบที่บัง")
root.geometry('1000x550')
#root.configure(bg="#B7EAF7")

Label(root, text="Welcome to").pack(padx=10, pady=10)
Label(root, text="'ทุกระบบจบที่บัง!'").pack(padx=10, pady=10)
def win():
    win = Tk()
    win.geometry("1000x550")

    Label(win, text="Rows:").grid(row=0)       
    Label(win, text="Columns:").grid(row=1)

    e1 = Entry(win)
    e2 = Entry(win)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    def show():
        print(e1.get())
        print(e2.get())
        e1.delete(0, "end")
        e2.delete(0, "end")

    Button(win, text="Get Info", width=10, command=show).grid(row=3, column=0, sticky= "w", padx=10, pady=5)
    Button(win, text="Exit", width=10, command=win.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)

    win.mainloop()

Button(root, text="Start!", command=win,).pack()
root.mainloop()