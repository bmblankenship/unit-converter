import tkinter as tk
from conversions import *

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x400")

def convert():
    input_field = float(input_var.get())

    input_unit = input_value.get()
    output_unit = output_value.get()

    output_var.set(str(calc_convert(input_unit, output_unit, input_field)))

def calc_convert(in_unit, out_unit, val):
    if in_unit == out_unit:
        return val
    else:
        match in_unit:
            case "Miles":
                return convert_miles(out_unit, val)

def convert_miles(out_unit, val):
    match out_unit:
        case "Kilometers":
            return val * miles_to_km()
        case "Feet":
            return val * miles_to_feet()
        case "Meters":
            return val * miles_to_meters()

# string variables
input_var = tk.StringVar()
output_var = tk.StringVar()

# Create Miles fields
input_label = tk.Label(root, text = "Input", font=('calibre', 10, 'bold'))
input_entry = tk.Entry(root,textvariable = input_var, font=('calibre', 10, 'normal'))

# Create Inches fields
output_label = tk.Label(root, text = "Output", font=('calibre', 10, 'bold'))
output_entry = tk.Entry(root,textvariable = output_var, font=('calibre', 10, 'normal'))

# Convert Button
convert_btn = tk.Button(root, text = 'Convert', command = convert)

# Input unit
input_options = ["Miles", "Kilometers", "Feet", "Meters"]
input_value = tk.StringVar(root)
input_value.set("Selection an Option")
input_menu = tk.OptionMenu(root, input_value, *input_options)

# Output unit
output_options = ["Miles", "Kilometers", "Feet", "Meters"]
output_value = tk.StringVar(root)
output_value.set("Selection an Option")
output_menu = tk.OptionMenu(root, output_value, *output_options)


# Place widgets
input_label.grid(row=1, column=0)
input_entry.grid(row=2, column=0)
input_menu.grid(row=3, column=0)

output_label.grid(row=1, column=2)
output_entry.grid(row=2, column=2)
output_menu.grid(row=3, column=2)

convert_btn.grid(row=4, column=1)

# Start the GUI event Loop
root.mainloop()