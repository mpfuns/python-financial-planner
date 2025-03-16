class NumberHandler:
# This function checks if a string is a number with a comma for this class
    def is_number(s):
        try:
            withoutCommaList= s.split(",")
            numberTogether= "".join(withoutCommaList)
            float(numberTogether)
            return True
        except ValueError:
            return False