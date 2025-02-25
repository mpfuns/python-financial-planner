class NumberHandler:
    def __init__(self, value):
        self.value = value

    def is_number(self):
        try:
            float(self.value)
            return True
        except ValueError:
            return False