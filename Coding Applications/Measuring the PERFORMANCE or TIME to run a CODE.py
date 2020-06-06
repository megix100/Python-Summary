print("\n Using Decorator to measure the PERFORMANCE or TIME that takes for the machine to execute a code")
from time import time

def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"It took {t2 - t1} s to perform this code")
    return wrap_func

@performance #YOUR CODE TO MEASURE THE PERFORMANCE GOES AFTER THIS LINE
def tot():
    total = 0
    for i in range(1000000):
        total += 5 * i
    print(total)

tot()