import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer")
window.minsize(width = 200, height = 50)
window.config(padx = 20, pady = 20)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text = str(km))

#Input
miles_input = tkinter.Entry(width = 7)
miles_input.grid(column = 1, row = 0)

#Miles Label
miles_label = tkinter.Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

#KM Label
km_label = tkinter.Label(text = "KM")
km_label.grid(column = 2, row = 1)

#Is Equal To

is_equal_label = tkinter.Label(text = "is equals to")
is_equal_label.grid(column = 0, row = 1)

#KM Result

km_result_label = tkinter.Label(text = "0")
km_result_label.grid(column = 1, row = 1)

# Calculate 

calculate_button = tkinter.Button(text = "Calculate", command = miles_to_km)
calculate_button.grid(column = 1, row = 2)




window.mainloop()
