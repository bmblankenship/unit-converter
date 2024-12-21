from tkinter import *
from tkinter import ttk

#def convert():
    #input_value = float(input_entry.get())
    #from_unit = front_unit_var.get()
    #to_unit = to_unit_var.get()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    frm = ttk.Frame(root, padding = 10)
    frm.grid()
    measureSystem = StringVar()
    metricChanged = StringVar()

    ttk.Checkbutton(frm, text="Use Metric", command = metricChanged, variable = measureSystem, onvalue = "metric", offvalue = "imperial").grid(column = 2, row = 2)
    ttk.Label(frm, text = "Hello World!").grid(column = 0, row = 0)
    ttk.Button(frm, text = "Quit", command = root.destroy).grid(column = 1, row = 0)
    ttk.Button(frm, text = "Convert").grid(column = 1, row = 1)
    root.mainloop()

