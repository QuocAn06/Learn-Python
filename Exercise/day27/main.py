import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 20, "bold"))
my_label.pack(side="left")
#my_label.pack(side="bottom")
#my_label.pack(expand=True)

# my_label["text"] = "New text"
my_label.config(text="New text")

window.mainloop()

# def bar(spam, eggs):
#     print(spam, eggs)
#
# bar(1, 2)