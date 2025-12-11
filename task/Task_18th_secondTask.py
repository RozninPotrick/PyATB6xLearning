# Q - Create a framework base counter that counts test execution instances:
class TestExecutionCounter:

    count = 0

    def __init__(self):
        TestExecutionCounter.count += 1

t1 = TestExecutionCounter()
t2 = TestExecutionCounter()
print(t2.count)