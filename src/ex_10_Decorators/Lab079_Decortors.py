def add_security(func):

    def wrapper():
        print("1. Before the function is called.")
        print("2. Add Helmet, dashcash, gloves, knee guards, license")
        func()
        print("3. After the function is called.")
        print("4. Secure Driving, Leave all the iteams")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("I'm driving ola scooter")

@add_security
def drive_zypp_scooter():
    print("I'm driving zypp scooter")



