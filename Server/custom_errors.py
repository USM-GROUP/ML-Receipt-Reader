class invalid_param(Exception):
    def __init__(self):
        self.message = "error: one or both of your parameters for 'get_slope' is invalid."

    def __str__(self):
        return self.message

class not_on_line(Exception):
    def __init__(self):
        self.message = "error: the price point was not on line"

    def __str__(self):
        return self.message