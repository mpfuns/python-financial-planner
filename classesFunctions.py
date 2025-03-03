class NumberHandler:
   
    def is_number(s):
        try:
            withoutCommaList= s.split(",")
            numberTogether= "".join(withoutCommaList)
            float(numberTogether)
            return True
        except ValueError:
            return False