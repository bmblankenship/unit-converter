def length_convert(input_unit, output_unit, val):
    """
    :String input_unit: Plural of input unit with leading capitol letter eg: Miles
    :String output_unit: Plural of output unit with leading capitol letter eg: Kilometers
    :float val: Input value to be converted to desired output unit
    :return: returns calculated value from an internal function in length_conversion.py
    """
    match input_unit:
        case "Miles":
            return convert_miles(output_unit, val)
        case "Kilometers":
            return convert_kilometers(output_unit, val)
        case "Feet":
            return convert_feet(output_unit, val)
        case "Meters":
            return convert_meters(output_unit, val)
        case "Centimeters":
            return convert_centimeters(output_unit, val)
        case "Millimeters":
            return convert_millimeters(output_unit, val)
        case "Yards":
            return convert_yards(output_unit, val)
        case "Inches":
            return convert_inches(output_unit, val)

def convert_miles(unit, val):
    match unit:
        case "Kilometers":
            return round(val * 1.60934, 2)
        case "Feet":
            return round(val * 5280, 2)
        case "Meters":
            return round(val * 1609.34, 2)
        case "Miles":
            return val
        case "Centimeters":
            return round(val * 1609.34 * 100, 2)
        case "Millimeters":
            return round(val * 1609.34 * 1000, 2)
        case "Yards":
            return round(val * 1760, 2)
        case "Inches":
            return round(val * 63360, 2)

def convert_kilometers(unit, val):
    match unit:
        case "Miles":
            return round(val * 0.621371, 2)
        case "Feet":
            return round(val * 3280.84, 2)
        case "Meters":
            return round(val * 1000, 2)
        case "Kilometers":
            return val
        case "Centimeters":
            return round(val * 100000, 2)
        case "Millimeters":
            return round(val * 1000000, 2)
        case "Yards":
            return round(val * 1093.61, 2)
        case "Inches":
            return round(val * 39370.1, 2)

def convert_feet(unit, val):
    match unit:
        case "Miles":
            return round(val * 0.000189394, 2)
        case "Kilometers":
            return round(val * 0.0003048, 2)
        case "Meters":
            return round(val * 0.3048, 2)
        case "Feet":
            return val
        case "Centimeters":
            return round(val * 30.48, 2)
        case "Millimeters":
            return round(val * 304.8, 2)
        case "Yards":
            return round(val / 3, 2)
        case "Inches":
            return round(val * 12, 2)

def convert_meters(unit, val):
    match unit:
        case "Miles":
            return round(val * 0.000621371, 2)
        case "Kilometers":
            return round(val * 0.001, 2)
        case "Feet":
            return round(val * 3.28084, 2)
        case "Meters":
            return val
        case "Centimeters":
            return round(val * 100, 2)
        case "Millimeters":
            return round(val * 1000, 2)
        case "Yards":
            return round(val * 1.09361, 2)
        case "Inches":
            return round(val * 39.3701, 2)

def convert_centimeters(unit, val):
    match unit:
        case "Miles":
            return round(val / 160900, 2)
        case "Kilometers":
            return round(val / 100000, 2)
        case "Feet":
            return round(val * 0.0328084, 2)
        case "Meters":
            return round(val * 0.01, 2)
        case "Centimeters":
            return val
        case "Millimeters":
            return round(val * 10, 2)
        case "Yards":
            return round(val * 0.0109361, 2)
        case "Inches":
            return round(val * 0.393701, 2)

def convert_millimeters(unit, val):
    match unit:
        case "Miles":
            return round(val / 1609000, 2)
        case "Kilometers":
            return round(val / 1000000, 2)
        case "Feet":
            return round(val / 304.8, 2)
        case "Meters":
            return round(val * 0.001, 2)
        case "Centimeters":
            return round(val * 10, 2)
        case "Millimeters":
            return val
        case "Yards":
            return round(val / 914.4, 2)
        case "Inches":
            return round(val * 0.0393701, 2)

def convert_yards(unit, val):
    match unit:
        case "Miles":
            return round(val / 1760, 2)
        case "Kilometers":
            return round(val / 1094, 2)
        case "Feet":
            return round(val * 3, 2)
        case "Meters":
            return round(val * 0.9144, 2)
        case "Centimeters":
            return round(val * 91.44, 2)
        case "Millimeters":
            return round(val * 914.4, 2)
        case "Yards":
            return val
        case "Inches":
            return round(val * 36, 2)

def convert_inches(unit, val):
    match unit:
        case "Miles":
            return round(val / 63360, 2)
        case "Kilometers":
            return round(val / 39370, 2)
        case "Feet":
            return round(val / 12, 2)
        case "Meters":
            return round(val / 39.37, 2)
        case "Centimeters":
            return round(val * 2.54, 2)
        case "Millimeters":
            return round(val * 25.4, 2)
        case "Yards":
            return round(val / 36, 2)
        case "Inches":
            return val