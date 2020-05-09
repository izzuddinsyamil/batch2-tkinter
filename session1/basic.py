import tkinter

window = tkinter.Tk()

window.geometry("321x200")

frame = tkinter.LabelFrame(window, text="label")
frame.pack()

label = tkinter.Label(frame, text="Hello world")
label.pack()


tkinter.Label(window, text="lab1").pack()

lab2 = tkinter.Label(window, text="lab2")
lab2.pack()

f = tkinter.LabelFrame(window, text="frame2")
f.pack()


tkinter.Label(f, text="new lab").grid()

window.mainloop()