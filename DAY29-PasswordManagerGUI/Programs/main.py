from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY29-PasswordManagerGUI/Resources/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

window.mainloop()
