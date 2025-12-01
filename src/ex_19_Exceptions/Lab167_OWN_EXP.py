def vwo_login(user):
    if user != "Admin":
        raise Exception("unauthorised Access!")
    return "Welcome"

print(vwo_login("pp"))
