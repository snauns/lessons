import warnings
"""
while True:

    try:

        digit1 = 10
        #warnings.warn("\nPossible zero devision!\n")
        digit2 = int(input("Enter digit: "))
        res = digit1/digit2
        print(res)
    except ZeroDivisionError as zde:
        print(f"Custom procces{zde}")
    except Exception as ex:
        print(ex)
    y = input("Enter Y for continue or N for stop")
    if(y.lower() == "n"):
        break
print("Cycle while has stopped!")
"""
from classes.buildingerror import BuildingError
from classes.validation import Validation
limit = 10
amount = int(input("Enter amount: "))
check = Validation(amount, limit)
try:
    check.Check()
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except BuildingError as be:
        print(f"Custom error message\n"
        f"{be}")
    except Exception as ex:
        print(ex)
