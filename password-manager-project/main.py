from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- CONSTANTS ------------------------------- #
NAME_OF_APP = "Password Manager"
BLUE = "#cce5ff"
FONT_NAME = "Courier"
EXAMPLE_EMAIL = "abc@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if (len(website) == 0) or (len(password) == 0) or (len(email) == 0):
        messagebox.askquestion(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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
generate_password_button = Button(text="Generate Password", font=(FONT_NAME, 8))
generate_password_button.grid(row=3, column=2, pady=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
