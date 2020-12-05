import tkinter as tk
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

FONT_NAME = "Courier"
IMAGE = "./day_22-30/day_29/logo.png"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Whoops", message= "Do not leave fields blank !")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \nUsername: {username} \nPassword: {password}")
        if is_ok:
            with open("./day_22-30/day_29/data.txt", "a") as f:
                f.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, tk.END)
                password_input.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

## Image of Tomato
canvas = tk.Canvas(width = 200, height = 200)
logo = tk.PhotoImage(file = IMAGE)
canvas.create_image(100, 100, image = logo)
canvas.grid(column = 1, row = 0)

# Website Related
website_label = tk.Label(text = "Website: ")
website_label.grid(column = 0, row = 1)

website_input = tk.Entry(width = 35)
website_input.grid(column = 1, row = 1, columnspan = 2)
website_input.focus()

# Email/Username Related
username_label = tk.Label(text = "Email/Username: ")
username_label.grid(column = 0, row = 2)

username_input = tk.Entry(width = 35)
username_input.grid(column = 1, row = 2, columnspan = 2)
username_input.insert(0, "test@test.com")

# Password related
password_label = tk.Label(text = "Password: ")
password_label.grid(column = 0, row = 3)

password_input = tk.Entry(width = 21)
password_input.grid(column = 1, row = 3)

password_generate = tk.Button(text = "Generate Password", command = generate_password)
password_generate.grid(column = 2, row = 3)

# Add Button
add_button = tk.Button(text = "Add", width = 36, command = save_password)
add_button.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()