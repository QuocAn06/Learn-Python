from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# #Label
# my_label = Label(text="I Am a Label", font=("Arial", 20, "bold"))
# my_label.pack()
# #my_label.pack(side="bottom")
# #my_label.pack(expand=True)
#
# # my_label["text"] = "New text"
# my_label.config(text="New text.")
#
# #Button
#
# def button_clicked():
#     # print("I got clicked.")
#     # my_label.config(text="Button Got Clicked.")
#     my_label.config(text=entry.get())
#
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
# #Entries
#
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# print(entry.get())
# entry.pack()
#
# #Text
#
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Examle of multi-line text entry.")
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     print(spinbox.get())
#
# spinbox = Spinbox(from_= 0, to= 10, width= 5,command= spinbox_used)
# spinbox.pack()
#
# #Scale
#
# def scale_used(value):
#     print(value)
#
# scale = Scale(from_=0, to= 100, command= scale_used)
# scale.pack()
#
# #Checkbutton
#
# def checkbutton_used():
#     print(checked_state.get())
#
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable= checked_state, command= checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #RadioButton
#
# def radio_used():
#     print(radio_state.get())
#
# radio_state = IntVar()
# radioButton1 = Radiobutton(text="Option 01", value=1, variable=radio_state, command=radio_used)
# radioButton2 = Radiobutton(text="Option 02", value=2, variable=radio_state, command=radio_used)
# radioButton1.pack()
# radioButton2.pack()
#
# #Listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
#
# window.mainloop()

# def bar(spam, eggs):
#     print(spam, eggs)
#
# bar(1, 2)

# #Place Method
# my_label = Label(text="New Text", font=("Arial", 20, "bold"))
# my_label.place(x=200, y=100)

#Grid Method
my_label_01 = Label(text="col= 0, row= 0", font=("Arial", 20, "bold"))
my_label_01.grid(column=0, row=0)
my_label_01.config(padx=50)

my_label_02 = Label(text="col= 2, row= 0", font=("Arial", 14, "bold"))
my_label_02.grid(column=2, row=0)

my_label_03 = Label(text="col= 1, row= 1", font=("Arial", 14, "bold"))
my_label_03.grid(column=1, row=1)

my_label_04 = Label(text="col= 3, row= 2", font=("Arial", 14, "bold"))
my_label_04.grid(column=3, row=2)
my_label_04.config(pady=50)

window.mainloop()