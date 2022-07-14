"""
a = input("What is your name?\n")
b = input("How much do you earn?\n")
if int(b) == 0:
    raise ZeroDivisionError("Can't proceed further")
if a.isnumeric():
    raise Exception("Numbers are not allowed")

# print(f"Hello,{a}")
#print(f"\tYou earn {b} Quadrillion Dollar")
"""

c = input("Enter your name : ")
try:
    print(a)

except Exception as e:
    if c == "Bharat":
        raise ValueError("Bharat is the CEO , Action is not allowed")

    print("Exception handled")
