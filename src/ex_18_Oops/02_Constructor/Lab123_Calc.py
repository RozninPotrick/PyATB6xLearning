class Calc:

        def __init__(self, a,b):
            self.a = a
            self.b = b

        def sum(self,a,b):
            return self.a + self.b

        def sub(self,a,b):
            return self.a - self.b

        def mul(self,a,b):
            return self.a * self.b

        def div(self,a,b):
            return self.a / self.b

calc_ref = Calc(3,5)
print(calc_ref.sum(3,5))
print(calc_ref.sub(3,5))
print(calc_ref.mul(3,5))
print(calc_ref.div(3,5))