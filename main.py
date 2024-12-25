import tkinter as tk

class UnitConverter:

    def __init__(self):
        # Create Main Window
        self.window_width = 600
        self.window_height = 400
        self.root = tk.Tk()
        self.root.title("Unit Converter")
        self.root.geometry("{}x{}".format(self.window_width, self.window_height))

        # String Variables
        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar()

        # Create Fonts
        self.bold_font = ('calibre', 10, 'bold')
        self.normal_font = ('calibre', 10, 'normal')

        # Create Input Labels
        self.input_label = tk.Label(self.root, text="Input", font=self.bold_font)
        self.input_entry = tk.Entry(self.root, textvariable=self.input_var, font=self.normal_font)
        self.input_options = unit_list()
        self.input_value = tk.StringVar(self.root)
        self.input_value.set("Select Input Unit")
        self.input_menu = tk.OptionMenu(self.root, self.input_value, *self.input_options)

        # Create Output fields
        self.output_label = tk.Label(self.root, text="Output", font=self.bold_font)
        self.output_entry = tk.Entry(self.root, textvariable=self.output_var, font=self.normal_font)
        self.output_options = unit_list()
        self.output_value = tk.StringVar(self.root)
        self.output_value.set("Select Output Unit")
        self.output_menu = tk.OptionMenu(self.root, self.output_value, *self.output_options)

        # Convert Button
        self.convert_btn = tk.Button(self.root, text='Convert', command= self.convert)

    def start_converter(self):
        self.place_widgets()
        self.root.mainloop()

    def place_widgets(self):
        # Place widgets

        self.input_label.place(relx=0.25, rely=0.4, anchor="n")
        self.input_entry.place(relx=0.25, rely=0.5, anchor="n")
        self.input_menu.place(relx=0.25, rely=0.6, anchor="n")

        self.output_label.place(relx=0.75, rely=0.4, anchor="n")
        self.output_entry.place(relx=0.75, rely=0.5, anchor="n")
        self.output_menu.place(relx=0.75, rely=0.6, anchor="n")

        self.convert_btn.place(relx=0.5, rely=0.9, anchor="n")

    def convert(self):
        input_field = float(self.input_var.get())
        self.output_var.set(str(self.calc_convert(input_field)))

    def calc_convert(self, val):
        if self.input_value == self.output_value:
            return val
        else:
            match self.input_value:
                case "Miles":
                    return self.convert_miles(val)
                case "Kilometers":
                    return self.convert_kilometers(val)
                case "Feet":
                    return self.convert_feet(val)
                case "Meters":
                    return self.convert_meters(val)

    def convert_miles(self, val):
        match self.output_value:
            case "Kilometers":
                return round(val * 1.60934, 2)
            case "Feet":
                return round(val * 5280, 2)
            case "Meters":
                return round(val * 1609.34, 2)

    def convert_kilometers(self, val):
        match self.output_value:
            case "Miles":
                return round(val * 0.621371, 2)
            case "Feet":
                return round(val * 3280.84, 2)
            case "Meters":
                return round(val * 1000, 2)

    def convert_feet(self, val):
        match self.output_value:
            case "Miles":
                return round(val * 0.000189394, 2)
            case "Kilometers":
                return round(val * 0.0003048, 2)
            case "Meters":
                return round(val * 0.3048, 2)

    def convert_meters(self, val):
        match self.output_value:
            case "Miles":
                return round(val * 0.000621371, 2)
            case "Kilometers":
                return round(val * 0.001, 2)
            case "Feet":
                return round(val * 3.28084, 2)

def unit_list():
    return["Miles", "Kilometers", "Feet", "Meters",
        "Quarts", "Liters", "Gallons", "Milliliters",
        "Pounds", "Kilograms"]

if __name__ == '__main__':
    uc = UnitConverter()
    uc.start_converter()