import tkinter

windows = tkinter.Tk()
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label.", font=("Arial", 20, "bold"))
# pack() function is used to display the label on screen, by default in the middle.
my_label.pack()
# Change the property
my_label.config(text='New Text')
my_label['text'] = 'Abhilash'


# Button

def button_command():
    print("I got clicked.")
    my_label['text'] = "Clicked"
    my_label.config(text=text_area.get())


button = tkinter.Button(text="Click Me", command=button_command)
button.pack()

# Entry

text_area = tkinter.Entry(width=10)
text_area.pack()

windows.mainloop()
