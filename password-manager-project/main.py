from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
NAME_OF_APP = "Password Manager"
BLUE = "#cce5ff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(NAME_OF_APP)
window.config(padx=20, pady=20, bg=BLUE)

canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
lock_img = PhotoImage(file="./img/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)

window.mainloop()