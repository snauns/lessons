def error_handling_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print("Error:", e)
    return wrapper

def calculate(expression):
    return eval(expression)

calculate = error_handling_decorator(calculate)

math_exp = input("Enter math expression: ")
print(math_exp, "=", calculate(math_exp))

#вибачте я забув зберегти класну роботу та я не можу зробити доп.завдання
