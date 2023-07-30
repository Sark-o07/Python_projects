# algorithm #
# input binary numbers and convert to integer#
# count the string of binary numbers input, subtract 1 and assign it to the starting power of the most significant bits#
# create a for loop to multiply each digit in the binary number with its respective weight based on its position
# sum all the products of each digits with it's respective weight.
from tkinter import *

window = Tk()
window.title("Binary to Decimal converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)
# Entry
input_1 = Entry(width=10)
# Add some text to begin with
input_1.insert(END, string="0")
input_1.grid(column=1, row=0)

# Label
label_1 = Label(text="is equals to", font=("Helvetica", 14, "italic"))
label_1.grid(column=0, row=1)
label_1.config(padx=5, pady=5)

label_2 = Label(text="Binary", font=("Helvetica", 14, "italic"))
label_2.grid(column=2, row=0)
label_2.config(padx=5, pady=5)

label_3 = Label(text="0", font=("Helvetica", 14))
label_3.grid(column=1, row=1)
label_3.config(padx=5, pady=5)
label_4 = Label(text="Decimal", font=("Helvetica", 14, "italic"))

label_4.grid(column=2, row=1)
label_4.config(padx=5, pady=5)

def calculate():
    # It converts the binary to Decimal
    decimal_number = 0
    binary_number = input_1.get()
    power = len(binary_number)
    for i in binary_number:
        power -= 1
        digit = int(i)
        product = (digit * (2 ** power))
        decimal_number += product
    label_3["text"] = decimal_number


# Button
button_1 = Button(text="calculate", command=calculate)
button_1.grid(column=1, row=2)



window.mainloop()




