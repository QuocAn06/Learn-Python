from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609)
    label_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")

entry.grid(column=1, row=0)

label_01 = Label(width=10)
label_01.config(text="Miles")
label_01.grid(column=2, row=0)

label_02 = Label(width=10)
label_02.config(text="is equal to")
label_02.grid(column=0, row=1)

label_result = Label(width=10)
label_result.config(text="0")
label_result.grid(column=1, row=1)

label_03 = Label(width=10)
label_03.config(text="Km")
label_03.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
