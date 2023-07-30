from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
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

label_2 = Label(text="Miles", font=("Helvetica", 14, "italic"))
label_2.grid(column=2, row=0)
label_2.config(padx=5, pady=5)

label_3 = Label(text="0", font=("Helvetica", 14))
label_3.grid(column=1, row=1)
label_3.config(padx=5, pady=5)
label_4 = Label(text="Km", font=("Helvetica", 14, "italic"))

label_4.grid(column=2, row=1)
label_4.config(padx=5, pady=5)

def calculate():
    # It converts the miles to Km
    user_input = int(input_1.get())
    convert = user_input * 1.609
    label_3["text"] = round(convert, 2)


# Button
button_1 = Button(text="calculate", command=calculate)
button_1.grid(column=1, row=2)



window.mainloop()
