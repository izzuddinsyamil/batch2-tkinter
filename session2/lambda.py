from tkinter import *

window = Tk()

window.geometry('300x300')

def callback(number):
    print("button ", number)

Button(window, text="one", command=lambda: callback(1)).pack()
Button(window, text="two", command=lambda: callback(2)).pack()
Button(window, text="three", command=lambda: callback(3)).pack()

window.mainloop()