from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# Entry
input = Entry(width=10)
print(input.get())
input.grid(row=0, column=1)


# Label
label_miles = Label(text="Miles", font=("Arial", 16, "bold"))
label_miles.grid(row=0, column=2)
label_miles.config(padx=5, pady=5)

label_equal_to = Label(text="Is equal to", font=("Arial", 16, "bold"))
label_equal_to.grid(row=1, column=0)
label_equal_to.config(padx=5, pady=5)

label_converted = Label(text="0", font=("Arial", 16, "bold"))
label_converted.grid(row=1, column=1)
label_converted.config(padx=5, pady=5)

label_Km = Label(text="Km", font=("Arial", 16, "bold"))
label_Km.grid(row=1, column=2)
label_Km.config(padx=5, pady=5)


# Button
def miles_to_km():
    new_value = 1.609*float(input.get())
    label_converted.config(text=new_value)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
