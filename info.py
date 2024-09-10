from tkinter import *
from tkinter import messagebox


def show_info():
    messagebox.showinfo("Oops", "there was an unknown error")

def show_warning():
    messagebox.showwarning("Somethings wrong", "this is a warning message")

def show_error():
    messagebox.showerror("Error", "there was an unknown error")

def question():
    response = messagebox.askquestion("question", "would you like to proceed?")
    messagebox.showinfo("Response", f"your response is: {response}")

def yes_no_cancel():
    option = messagebox.askyesnocancel("Option", "do you want to save the changes?")
    if option is True:
        messagebox.showinfo("Saving", "all changes were succesfully saved")
    elif option is False:
        messagebox.showinfo("Reverting", "all changes were returned to default")
    else:
        messagebox.showinfo("Canceling", "terminating everything")

scr = Tk()

scr.title="info_box"

but1 = Button(scr, text="show info", command=show_info)
but1.pack()

but2 = Button(scr, text="warning", command=show_warning)
but2.pack()

but3 = Button(scr, text="question", command=question)
but3.pack()

but4 = Button(scr, text="option", command=yes_no_cancel)
but4.pack()



scr.mainloop()


