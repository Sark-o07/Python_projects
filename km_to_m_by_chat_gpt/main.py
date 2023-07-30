from tkinter import *


def convert():
    # get value from entry widget
    km = float(entry.get())

    # convert km to meters
    m = km * 1000

    # set the value in output label
    output.config(text=m)


root = Tk()
root.title("Kilometers to Meters Converter")

# create input label and entry widget
Label(root, text="Enter kilometers: ").grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# create button for conversion
button = Button(root, text="Convert", command=convert)
button.grid(row=1, column=0)

# create output label for converted value
Label(root, text="Meters: ").grid(row=2, column=0)
output = Label(root, text="")
output.grid(row=2, column=1)

root.mainloop()

