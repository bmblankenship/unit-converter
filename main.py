import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Unit Converter")
    root.geometry("600x400")

    # string variables
    input_var = tk.StringVar()
    output_var = tk.StringVar()

    # Create Input fields
    input_label = tk.Label(root, text="Input", font=('calibre', 10, 'bold'))
    input_entry = tk.Entry(root, textvariable=input_var, font=('calibre', 10, 'normal'))
    input_options = input_list()
    input_value = tk.StringVar(root)
    input_value.set("Selection an Option")
    input_menu = tk.OptionMenu(root, input_value, *input_options)

    # Create Output fields
    output_label = tk.Label(root, text="Output", font=('calibre', 10, 'bold'))
    output_entry = tk.Entry(root, textvariable=output_var, font=('calibre', 10, 'normal'))
    output_options = output_list()
    output_value = tk.StringVar(root)
    output_value.set("Selection an Option")
    output_menu = tk.OptionMenu(root, output_value, *output_options)

    # Convert Button
    convert_btn = tk.Button(root, text='Convert', command=lambda: convert(input_var, input_value, output_value, output_var))

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

def input_list():
    return ["Miles", "Kilometers", "Feet", "Meters"]

def output_list():
    return ["Miles", "Kilometers", "Feet", "Meters"]

def convert(input_var, input_value, output_value, output_var):
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
            case "Kilometers":
                return convert_kilometers(out_unit, val)
            case "Feet":
                return convert_feet(out_unit, val)
            case "Meters":
                return convert_meters(out_unit, val)

def convert_miles(out_unit, val):
    match out_unit:
        case "Kilometers":
            return round(val * 1.60934, 2)
        case "Feet":
            return round(val * 5280, 2)
        case "Meters":
            return round(val * 1609.34, 2)

def convert_kilometers(out_unit, val):
    match out_unit:
        case "Miles":
            return round(val * 0.621371, 2)
        case "Feet":
            return round(val * 3280.84, 2)
        case "Meters":
            return round(val * 1000, 2)

def convert_feet(out_unit, val):
    match out_unit:
        case "Miles":
            return round(val * 0.000189394, 2)
        case "Kilometers":
            return round(val * 0.0003048, 2)
        case "Meters":
            return round(val * 0.3048, 2)

def convert_meters(out_unit, val):
    match out_unit:
        case "Miles":
            return round(val * 0.000621371, 2)
        case "Kilometers":
            return round(val * 0.001, 2)
        case "Feet":
            return round(val * 3.28084, 2)

if __name__ == '__main__':
    main()