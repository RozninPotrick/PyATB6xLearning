class Calc:


    def __init__(self):
        print("DC")

    def sum(self, a , b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

a = 10
# a = float(input("Enter a number"))
b = 20
# b = float(input("Enter a number"))

calc_ref = Calc()

output_sum = calc_ref.sum(a,b)
output_sub = calc_ref.sub(a,b)
output_mul = calc_ref.mul(a,b)
outpou_div = calc_ref.div(a,b)

print(output_sum,  output_sub, output_mul, outpou_div)


