import tkinter

windows = tkinter.Tk()
windows.title("My First GUI Program")
windows.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label.", font=("Arial", 20, "bold"))
# pack() function is used to display the label on screen, by default in the middle.
my_label.pack()

windows.mainloop()
