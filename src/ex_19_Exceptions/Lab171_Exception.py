# python 3.11
eg = ExceptionGroup("Multiple EX", [
    ValueError("Invalid Value"),
    TypeError("TypeError"),
    ZeroDivisionError("Cant't divide by zero")
])


def check_div(a):
    if a == 0:
        raise eg
