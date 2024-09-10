from tkinter import *
from tkinter import messagebox
import time

scr = Tk()
scr.title("Timer")
scr.geometry("300x300")

hour = StringVar()
min = StringVar()
sec = StringVar()

hour.set("00")
min.set("00")
sec.set("00")


hour_input = Entry(scr, font="Times", width=3, textvariable=hour)
hour_input.place(x=80, y=100)
min_input = Entry(scr, font="Times", width=3, textvariable=min)
min_input.place(x=130, y=100)
sec_input = Entry(scr, font="Times", width=3, textvariable=sec)
sec_input.place(x=180, y=100)

#count = 
countbut = Button(scr, text="start countdown", command="")
countbut.place(x=100, y=200)

scr.mainloop()