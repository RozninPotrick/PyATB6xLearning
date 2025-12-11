class MathOperation:

    def div(self, a, b):
        return a / b

    @staticmethod
    def sum(a,b):
        return a / b

t = MathOperation()
print(t.div(2,3))
print(t.sum(2,3))

print(MathOperation.sum(2,3))
print(MathOperation.div(2,3,6))
