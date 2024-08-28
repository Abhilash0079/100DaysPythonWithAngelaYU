from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = id_input.get()
    password = pass_input.get()

    with open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY29-PasswordManagerGUI/Resources/data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password} \n")
        web_input.delete(0, END)
        pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY29-PasswordManagerGUI/Resources/logo.png")
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

gen_button = Button(text="Generate Password", width=16)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
