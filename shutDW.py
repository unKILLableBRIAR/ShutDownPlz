from tkinter import *
import os

win = Tk()
win.title("SHUTDOWN PROGRAM")
win.geometry("200x200")
win.resizable = False, False
def shutdw():
    os.system("shutdown -t 0")

def restnw():
    os.system("shutdown -r -t 0")

btn1 = Button(win, text = "SHUT DOWN NOW", command = shutdw)
btn1.pack()

btn2 = Button(win, text = "RESTART NOW", command = restnw)
btn2.pack()

win.mainloop()