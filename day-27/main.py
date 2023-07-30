from tkinter import *
import playground

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
label_1 = Label(text="enter first number", font=("Helvetica", 16, "italic"))
label_1.grid(column=0, row=0)


def button_clicked():
    label_1["text"] = input_1.get()


# Button
button_1 = Button(text="click me", command=button_clicked)
button_1.grid(column=1, row=1)

button_2 = Button(text="click me too", command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
input_1 = Entry(width=10)
print(input_1.get())
input_1.grid(column=3, row=3)




window.mainloop()
