def convert_miles(unit, val):
    match unit:
        case "Kilometers":
            return round(val * 1.60934, 2)
        case "Feet":
            return round(val * 5280, 2)
        case "Meters":
            return round(val * 1609.34, 2)
        case "Miles":
            return round(val)


def convert_kilometers(unit, val):
    match unit:
        case "Miles":
            return round(val * 0.621371, 2)
        case "Feet":
            return round(val * 3280.84, 2)
        case "Meters":
            return round(val * 1000, 2)
        case "Kilometers":
            return round(val)


def convert_feet(unit, val):
    match unit:
        case "Miles":
            return round(val * 0.000189394, 2)
        case "Kilometers":
            return round(val * 0.0003048, 2)
        case "Meters":
            return round(val * 0.3048, 2)
        case "Feet":
            return round(val)


def convert_meters(unit, val):
    match unit:
        case "Miles":
            return round(val * 0.000621371, 2)
        case "Kilometers":
            return round(val * 0.001, 2)
        case "Feet":
            return round(val * 3.28084, 2)
        case "Meters":
            return round(val)