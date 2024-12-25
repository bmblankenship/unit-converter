def convert_pounds(unit, val):
    match unit:
        case "Kilograms":
            return round(val * 0.453592, 2)

def convert_kilograms(unit, val):
    match unit:
        case "Pounds":
            return round(val * 2.20462, 2)