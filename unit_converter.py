import tkinter as tk
from settings import Settings

class UnitConverter:

    def __init__(self):
        # Create Main Window
        self.set = Settings()
        self.root = tk.Tk()
        self.root.title("Unit Converter")
        self.root.geometry("{}x{}".format(self.set.window_width, self.set.window_height))

        # String Variables
        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.type_var = tk.StringVar(self.root, "0")

        # Type Selection
        self.type_length = tk.Radiobutton(self.root, text="Length", variable=self.type_var, value = "1", command=self.length_selected)
        self.type_volume = tk.Radiobutton(self.root, text="Volume", variable=self.type_var, value = "2", command=self.volume_selected)
        self.type_weight = tk.Radiobutton(self.root, text="Weight", variable=self.type_var, value = "3", command=self.weight_selected)

        # Create Inputs
        self.input_label = tk.Label(self.root, text="Input", font=self.set.bold_font)
        self.input_entry = tk.Entry(self.root, textvariable=self.input_var, font=self.set.normal_font)

        self.input_length_value = tk.StringVar(self.root)
        self.input_length_value.set("Length")
        self.input_length_menu = tk.OptionMenu(self.root, self.input_length_value, *self.set.length_options)
        self.input_length_menu.config(state="disabled")

        self.input_volume_value = tk.StringVar(self.root)
        self.input_volume_value.set("Volume")
        self.input_volume_menu = tk.OptionMenu(self.root, self.input_volume_value, *self.set.volume_options)
        self.input_volume_menu.config(state="disabled")

        self.input_weight_value = tk.StringVar(self.root)
        self.input_weight_value.set("Weight")
        self.input_weight_menu = tk.OptionMenu(self.root, self.input_weight_value, *self.set.weight_options)
        self.input_weight_menu.config(state="disabled")

        # to be deleted
        self.input_options = unit_list()
        self.input_value = tk.StringVar(self.root)
        self.input_value.set("Select Input Unit")
        self.input_menu = tk.OptionMenu(self.root, self.input_value, *self.input_options)

        # Create Outputs
        self.output_label = tk.Label(self.root, text="Output", font=self.set.bold_font)
        self.output_entry = tk.Entry(self.root, textvariable=self.output_var, font=self.set.normal_font)
        self.output_options = unit_list()
        self.output_value = tk.StringVar(self.root)
        self.output_value.set("Select Output Unit")
        self.output_menu = tk.OptionMenu(self.root, self.output_value, *self.output_options)

        # Convert Button
        self.convert_btn = tk.Button(self.root, text='Convert', command= self.convert)

    def length_selected(self):
        self.input_length_menu.config(state="normal")
        self.input_volume_menu.config(state="disabled")
        self.input_weight_menu.config(state="disabled")

    def volume_selected(self):
        self.input_length_menu.config(state="disabled")
        self.input_volume_menu.config(state="normal")
        self.input_weight_menu.config(state="disabled")

    def weight_selected(self):
        self.input_length_menu.config(state="disabled")
        self.input_volume_menu.config(state="disabled")
        self.input_weight_menu.config(state="normal")

    def start_converter(self):
        self.place_widgets()
        self.root.mainloop()

    def place_widgets(self):
        # Place widgets
        self.type_length.place(relx=0.25, rely=0.1, anchor="n")
        self.type_volume.place(relx=0.5, rely=0.1, anchor="n")
        self.type_weight.place(relx=0.75, rely=0.1, anchor="n")

        self.input_label.place(relx=0.25, rely=0.2, anchor="n")
        self.input_entry.place(relx=0.25, rely=0.3, anchor="n")
        self.input_menu.place(relx=0.25, rely=0.6, anchor="n")

        self.input_length_menu.place(relx=0.25, rely=0.7, anchor="n")
        self.input_volume_menu.place(relx=0.25, rely=0.8, anchor="n")
        self.input_weight_menu.place(relx=0.25, rely=0.9, anchor="n")

        self.output_label.place(relx=0.75, rely=0.2, anchor="n")
        self.output_entry.place(relx=0.75, rely=0.3, anchor="n")
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