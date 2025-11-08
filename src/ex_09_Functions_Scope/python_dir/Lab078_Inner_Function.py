def outer_function():
    var1 = 30

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function1():
        print(var1)

    inner_function()
    inner_function1()

outer_function()