names = ["QA","","Automation","","Tester"]

def remove(x):
    if x != "":
        return True
    return None

non_empty = list(filter(None, names))
print(non_empty)