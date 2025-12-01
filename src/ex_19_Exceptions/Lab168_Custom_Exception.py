class InvalidAgeException(Exception):
    pass

def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero") # built in raise error

def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking") # custom raise error


can_you_drink(25)
#can_you_drink(17)