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
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website", bg=BLUE)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username", bg=BLUE)
email_label.grid(row=2, column=0)

password_label = Label(text="Password", bg=BLUE)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
password_entry = Entry(width=21)

window.mainloop()
