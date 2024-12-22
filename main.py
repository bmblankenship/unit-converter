import tkinter as tk
import conversions as conv

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x400")

# string variables
input_var = tk.StringVar()
output_var = tk.StringVar()

def convert():
    input_field = input_var.get()
    output_field = output_var.get()

    print("Input: " + input_field)
    print("Output: " + output_field)

# Create Miles fields
input_label = tk.Label(root, text = "Input", font=('calibre', 10, 'bold'))
input_entry = tk.Entry(root,textvariable = input_var, font=('calibre', 10, 'normal'))

# Create Inches fields
output_label = tk.Label(root, text = "Output", font=('calibre', 10, 'bold'))
output_entry = tk.Entry(root,textvariable = output_var, font=('calibre', 10, 'normal'))

# Convert Button
convert_btn = tk.Button(root, text = 'Convert', command = convert)

# Create Input Unit Listbox
input_menu_button = tk.Menubutton(root, text = "Input Unit")
input_menu_button.menu = tk.Menu(input_menu_button)
input_menu_button["menu"] = input_menu_button.menu
ivar1 = tk.IntVar()
ivar2 = tk.IntVar()
ivar3 = tk.IntVar()

input_menu_button.menu.add_checkbutton(label = "Miles", variable = ivar1)
input_menu_button.menu.add_checkbutton(label = "Inches", variable = ivar1)
input_menu_button.menu.add_checkbutton(label = "Feet", variable = ivar1)

# place widgets
input_label.grid(row=1, column=0)
input_entry.grid(row=2, column=0)
input_menu_button.grid(row=3, column=0)

output_label.grid(row=1, column=2)
output_entry.grid(row=2, column=2)

convert_btn.grid(row=4, column=1)

# Start the GUI event Loop
root.mainloop()