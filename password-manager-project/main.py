from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
NAME_OF_APP = "Password Manager"
BLUE = "#cce5ff"
FONT_NAME = "Courier"
EXAMPLE_EMAIL = "abc@gmail.com"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(LETTERS) for _ in range(nr_letters)]
    password_symbols = [choice(SYMBOLS) for _ in range(nr_symbols)]
    password_numbers = [choice(NUMBERS) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if (len(website) == 0) or (len(password) == 0) or (len(email) == 0):
        messagebox.askquestion(title="Oops", message="Please don't leave any fields empty!")
    else:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

            if email != EXAMPLE_EMAIL:
                email_entry.delete(0, END)
                email_entry.insert(0, EXAMPLE_EMAIL)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(NAME_OF_APP)
window.config(padx=60, pady=60, bg=BLUE)

canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
lock_img = PhotoImage(file="./img/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=BLUE, font=(FONT_NAME, 11, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=BLUE, font=(FONT_NAME, 11, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=BLUE, font=(FONT_NAME, 11, "bold"))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=46)
website_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=2)
website_entry.focus()

email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=2)
email_entry.insert(0, EXAMPLE_EMAIL)

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1, padx=3, pady=2)

# Buttons
generate_password_button = Button(text="Generate Password", font=(FONT_NAME, 8), command=generate_password)
generate_password_button.grid(row=3, column=2, pady=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
