class Settings:
    """
    A class to store configuration settings for unit_converter.py
    """
    def __init__(self):
        # Window Settings
        self.window_width = 600
        self.window_height = 400

        # Font Settings
        self.bold_font = ('calibre', 10, 'bold')
        self.normal_font = ('calibre', 10, 'normal')

        # Menu Settings
        self.length_options = ["Miles", "Kilometers", "Feet", "Meters", "Centimeters", "Millimeters", "Yards", "Inches"]
        self.volume_options = ["Quarts", "Liters", "Gallons", "Milliliters"]
        self.weight_options = ["Pounds", "Kilograms"]