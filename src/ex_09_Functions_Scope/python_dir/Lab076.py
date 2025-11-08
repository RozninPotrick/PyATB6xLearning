public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(private_toilet)
    print(public_toilet)

home()

def strange():
    print(public_toilet)
    # print(private_toilet) you cant call this inner(Local) variable

strange()