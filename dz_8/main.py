import time


def calculate_time(function):
    start = time.time()
    function()
    end = time.time()
    return end - start

def zero_function():
    print("hello")
    time.sleep(1)

elapsed_time = int(calculate_time(zero_function))

if elapsed_time != 1:
    print("функція працює не вірно")