from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 20, "bold"))
my_label.pack()
#my_label.pack(side="bottom")
#my_label.pack(expand=True)

# my_label["text"] = "New text"
my_label.config(text="New text.")

#Button

def button_clicked():
    # print("I got clicked.")
    my_label.config(text="Button Got Clicked.")

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()

# def bar(spam, eggs):
#     print(spam, eggs)
#
# bar(1, 2)