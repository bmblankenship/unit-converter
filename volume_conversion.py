def convert_milliliters(unit, val):
    match unit:
        case "Liters":
            return round(val * 1000, 2)
        case "Gallons":
            return round(val * 0.000264172, 2)
        case "Quarts":
            return round(val * 0.00105669, 2)

def convert_gallons(unit, val):
    match unit:
        case "Liters":
            return round(val * 3.78541, 2)
        case "Quarts":
            return round(val * 4, 2)
        case "Milliliters":
            return round(val * 3785.41, 2)

def convert_liters(unit, val):
    match unit:
        case "Quarts":
            return round(val * 1.05669, 2)
        case "Gallons":
            return round(val * 0.264172, 2)
        case "Milliliters":
            return round(val * 1000, 2)

def convert_quarts(unit, val):
    match unit:
        case "Liters":
            return round(val * 0.946353, 2)
        case "Gallons":
            return round(val * 0.25, 2)
        case "Milliliters":
            return round(val * 946.353, 2)