"""
a = 7
def printjoke(str):
    print(f"this function is a joke{str}")
"""

# Classes - Template
# Object - Instance of the class
# DRY - Do not repeat yourself

class Student:
    pass

Bharat = Student()
Vivek = Student()
Shivam = Student()
Rohit = Student()

Bharat.name = "Bharat"
Bharat.Class = 12
Bharat.Section = "A"
Vivek.name = "Vivek"
Vivek.Class = 11
Vivek.Section = "B"
Shivam.name = "Shivam"
Shivam.Class = 10
Shivam.Section = "C"
Rohit.name = "Rohit"
Rohit.Class = 9
Rohit.Section = "D"

print(Bharat.name,Vivek.Section,Shivam.name,Rohit.Class)

