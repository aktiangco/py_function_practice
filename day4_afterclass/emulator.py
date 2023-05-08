# Activity: Currency Exchange Emulator
# *! To check: python3 day4_afterclass/emulator.py

class Currency:

    currencies =  {'CHF': 0.930023, #swiss franc 
                    'CAD': 1.264553, #canadian dollar
                    'GBP': 0.737414, #british pound
                    'JPY': 111.019919, #japanese yen
                    'EUR': 0.862361, #euro
                    'USD': 1.0} #us dollar
        
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
            An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    #add magic methods here
    def __repr__(self):
        #* Return the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
        return f"{round(self.value,2)} {self.unit}"

    def __str__(self):
        #* This method returns the same value as __repr__(self).
        return f"{round(self.value,2)} {self.unit}"

    def __add__(self,other):
        #* Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
        if type(other) == int or type(other) == float:
            x = (other * Currency.currencies[self.unit])
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
        return Currency(x + self.value, self.unit)

    def __iadd__(self, other):
        #* Define the '+=' operator.
        return Currency.__add__(self,other)

    def __radd__(self, other):
        #* Define the reverse '+' operator when the left operand is an int or a float.
        res = self + other
        if self.unit != "USD":
            res.changeTo("USD")
        return res

    def __sub__(self,other):
        #* Define the '-' operator. If other is an int or a float, other will be treated as a USD value.
        if type(other) == int or type(other) == float:
            x = (other * Currency.currencies[self.unit])
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        #* Define the '-=' operator.
        return Currency.__sub__(self,other)        
    
    def __rsub__(self, other):
        #* Define the reverse '-' operator when the left operand is an int or a float.
        res = other - self.value
        res = Currency(res,self.unit)
        if self.unit != "USD":
            res.changeTo("USD")
        return res
  

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2) # Result will be in EUR
print(v2 + v1) # Result will be in USD
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1) # Result will be in USD
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) # Result will be in USD 


