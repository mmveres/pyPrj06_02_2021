from tkinter import *
from tkinter import messagebox


def btn_click():
    str_var.set("Hi")
    value = int(message.get())
    value+=10
    messagebox.showinfo("GUI Python",str(value) )


if __name__ == '__main__':
    win = Tk()
    win.title("First win")
    win.geometry("400x500")

    message = StringVar()

    message_entry = Entry(textvariable=message)
    message_entry.place(relx=.5, rely=.1, anchor="c")

    str_var = StringVar()
    str_var.set("Ok")
    btn = Button(win,  textvariable=str_var, command = btn_click)
    btn.pack()
    win.mainloop()