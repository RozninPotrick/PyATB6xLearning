import time

def print_logs(func):

    def wrapper():
      print("start of the logs")
      func()
      print("end of the logs")
    return wrapper

def time_decorators(func):
    def wrapper():
        start_time  = time.time()
        print("start_time")
        func()
        end_time = time.time()
        print("end_time")
        print("Total time taken by function ->" , end_time - start_time)
    return wrapper()


@time_decorators
@print_logs
def test_ui1():
    print("Add a function,time taken by this function is 1")
    time.sleep(2)

@time_decorators
@print_logs
def test_ui2():
    print("Add a function,time taken by this function is 2")
    time.sleep(5)


