from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=600)

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
    # my_label.config(text="Button Got Clicked.")
    my_label.config(text=inputBox.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entries

entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
print(entry.get())
entry.pack()

#Text

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Examle of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_= 0, to= 10, width= 5,command= spinbox_used)
spinbox.pack()

#Scale

def scale_used(value):
    print(value)
scale = Scale(from_=0, to= 100, command= scale_used)
scale.pack()




window.mainloop()

# def bar(spam, eggs):
#     print(spam, eggs)
#
# bar(1, 2)