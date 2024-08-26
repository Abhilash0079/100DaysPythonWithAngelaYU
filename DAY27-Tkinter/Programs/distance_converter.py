from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def selection_changed(event):
    selection1 = combo1.get()
    my_label1.config(text=selection1)
    selection2 = combo2.get()
    my_label2.config(text=selection2)


def distance_converter():
    converter1 = combo1.get()
    converter2 = combo2.get()
    distance_input = float(input1.get())

    if converter1 == "Miles":
        if converter2 == "Miles":
            dist = (distance_input * 1)
            input2.config(text=f"{dist}")
        elif converter2 == "Kilometer":
            dist = (distance_input * 1.609)
            input2.config(text=f"{dist}")
        elif converter2 == "Meter":
            dist = (distance_input * 1609.344)
            input2.config(text=f"{dist}")
        elif converter2 == "Centimeter":
            dist = (distance_input * 160934.4)
            input2.config(text=f"{dist}")

    elif converter1 == "Kilometer":
        if converter2 == "Miles":
            dist = (distance_input / 1.609)
            input2.config(text=f"{dist}")
        elif converter2 == "Kilometer":
            dist = (distance_input * 1)
            input2.config(text=f"{dist}")
        elif converter2 == "Meter":
            dist = (distance_input * 1000)
            input2.config(text=f"{dist}")
        elif converter2 == "Centimeter":
            dist = (distance_input * 100000)
            input2.config(text=f"{dist}")

    elif converter1 == "Meter":
        if converter2 == "Miles":
            dist = (distance_input / 1609.344)
            input2.config(text=f"{dist}")
        elif converter2 == "Kilometer":
            dist = (distance_input / 1000)
            input2.config(text=f"{dist}")
        elif converter2 == "Meter":
            dist = (distance_input * 1)
            input2.config(text=f"{dist}")
        elif converter2 == "Centimeter":
            dist = (distance_input * 100)
            input2.config(text=f"{dist}")

    elif converter1 == "Centimeter":
        if converter2 == "Miles":
            dist = (distance_input / 160934.4)
            input2.config(text=f"{dist}")
        elif converter2 == "Kilometer":
            dist = (distance_input / 100000)
            input2.config(text=f"{dist}")
        elif converter2 == "Meter":
            dist = (distance_input / 100)
            input2.config(text=f"{dist}")
        elif converter2 == "Centimeter":
            dist = (distance_input * 1)
            input2.config(text=f"{dist}")


window = Tk()
window.title("Distance Converter")
window.minsize(width=300, height=200)

# Read the Image
image = Image.open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY27-Tkinter/Resources/converter.png")

# Resize the image using resize() method
resize_image = image.resize((50, 50))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.grid(column=1, row=0)

# Entry
input1 = Entry(width=15)
input1.grid(column=0, row=1)

# Dropdown
combo1 = ttk.Combobox(values=["Miles", "Kilometer", "Meter", "Centimeter"])
combo1.current(0)
combo1.bind("<<ComboboxSelected>>", selection_changed)
combo1.grid(column=1, row=1)

my_label1 = Label(text="Miles", font=("Arial", 14, "bold"))
my_label1.grid(column=2, row=1)

# Entry
input2 = Label(text='0')
input2.grid(column=0, row=2)

combo2 = ttk.Combobox(values=["Miles", "Kilometer", "Meter", "Centimeter"])
combo2.current(1)
combo2.bind("<<ComboboxSelected>>", selection_changed)
combo2.grid(column=1, row=2)

my_label2 = Label(text="Kilometer", font=("Arial", 14, "bold"))
my_label2.grid(column=2, row=2)

# Button
button = Button(text="Click Me", command=distance_converter)
button.grid(column=1, row=3)

window.mainloop()
