def before_after_ui_test(func):

    def wrapper():
        print("Before UI test Code")
        func()
        print("After UI test Code")

    return wrapper()



@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Test")