from tkinter import *

window = Tk()
window.geometry('500x300')


"""
dummy data
"""
dummy_apple = {
    "title": "Apple",
    "phone": 12345,
    "note": "dummy note"
}

dummy_mom = {
    "title": "mom",
    "phone": 3424235,
    "note": "dummy note"
}

dummy_uncle = {
    "title": "uncle",
    "phone": 998989,
    "note": "dummy note"
}


def change_value(data):
    contact_title['text'] = data['title']
    phone_value['text'] = data['phone']
    note_value['text'] = data['note']


"""
left side
"""
# left frame
left_frame = Frame(window)
left_frame.pack(side='left')
left_frame.place(width=150)

lf_upper = Frame(left_frame)
lf_upper.pack()
Entry(lf_upper).pack()

# lower part for left frame
lf_lower = Frame(left_frame)
lf_lower.pack(fill='both', expand='yes', pady=5)

Button(lf_lower, text='Apple', command=lambda: change_value(
    dummy_apple)).pack(fill='both', expand='yes')
Button(lf_lower, text='Mom', command=lambda: change_value(
    dummy_mom)).pack(fill='both', expand='yes')
Button(lf_lower, text='Uncle', command=lambda: change_value(
    dummy_uncle)).pack(fill='both', expand='yes')


"""
right side
"""

# right frame
right_frame = Frame(window)
right_frame.pack()

rf_upper = Frame(right_frame)
rf_upper.pack()

contact_title = Label(rf_upper, text='-')
contact_title.pack()

# lower part for right frame
rf_lower = Frame(right_frame)
rf_lower.pack()

phone_label = Label(rf_lower, text='Phone')
phone_label.grid(row=0, column=0)

note_label = Label(rf_lower, text='Note')
note_label.grid(row=1, column=0)

phone_value = Label(rf_lower, text='-')
phone_value.grid(row=0, column=1)

note_value = Label(rf_lower, text='-')
note_value.grid(row=1, column=1)

window.mainloop()
