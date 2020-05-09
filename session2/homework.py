from tkinter import *

window = Tk()

window.geometry('300x500')

# todo list section
list_label = LabelFrame(window, text="Todo List")
list_label.pack(fill='both', expand='yes')

# insert todo section
insert_label = LabelFrame(window, text="Insert Todo")
insert_label.pack(fill='both', expand='yes')

insert_entry = Entry(insert_label)
insert_entry.pack(side='left', padx=10)

insert_button = Button(insert_label, text="Submit")
insert_button.pack(side='left')

# delete todo section
delete_label = LabelFrame(window, text="Delete Todo")
delete_label.pack(fill='both', expand='yes')

delete_entry = Entry(delete_label)
delete_entry.pack(side='left', padx=10)

delete_button = Button(delete_label, text="Submit")
delete_button.pack(side='left')


# fill only
"""
list_todo = LabelFrame(window, text="Todo List")
list_todo.pack(fill='both')

Label(list_todo, text="list").pack()

insert_todo = LabelFrame(window, text="Insert Todo")
insert_todo.pack(fill='both')

Label(insert_todo, text="insert").pack()

delete_todo = LabelFrame(window, text="Delete Todo")
delete_todo.pack(fill='both')

Label(delete_todo, text="delete").pack()
"""

# expand only
"""
list_todo = LabelFrame(window, text="Todo List")
list_todo.pack(expand='yes')

Label(list_todo, text="list").pack()

insert_todo = LabelFrame(window, text="Insert Todo")
insert_todo.pack(expand='yes')

Label(insert_todo, text="insert").pack()

delete_todo = LabelFrame(window, text="Delete Todo")
delete_todo.pack(expand='yes')

Label(delete_todo, text="delete").pack()
"""

window.mainloop()
