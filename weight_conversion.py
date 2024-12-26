def weight_convert(input_unit, output_unit, val):
    match input_unit:
        case "Pounds":
            return convert_pounds(output_unit, val)
        case "Kilograms":
            return convert_kilograms(output_unit, val)

def convert_pounds(unit, val):
    match unit:
        case "Kilograms":
            return round(val * 0.453592, 2)

def convert_kilograms(unit, val):
    match unit:
        case "Pounds":
            return round(val * 2.20462, 2)