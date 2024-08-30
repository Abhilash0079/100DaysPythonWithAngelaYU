from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(3, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 5))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 3))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    # to copy the generated password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = id_input.get()
    password_field = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password_field,
        }
    }

    if len(website) == 0 or len(password_field) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty.")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password_field}\nIs it ok to save?")

        # if is_ok:
        try:
            with open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY30-PasswordManagerWithSearch/Resources/data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY30-PasswordManagerWithSearch/Resources/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY30-PasswordManagerWithSearch/Resources/data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY30-PasswordManagerWithSearch/Resources/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website :")
web_label.grid(column=0, row=1)

web_input = Entry(width=55)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

id_label = Label(text="Email/Username :")
id_label.grid(column=0, row=2)

id_input = Entry(width=55)
id_input.grid(column=1, row=2, columnspan=2)
id_input.insert(0, "abhilashkumar213@gmail.com")

pass_label = Label(text="Password :")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=34)
pass_input.grid(column=1, row=3)

gen_button = Button(text="Generate Password", width=16, command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
