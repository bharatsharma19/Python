"""
def function1():
    print("Hello")

func2 = function1
del function1
func2()
"""
"""
def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = funcret(1)
print(a)
"""
"""
def executor(func):
    func("This")

executor(print)
"""

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

def who_is_bharat():
    print("Bharat is a good boy")

who_is_bharat = dec1(who_is_bharat)
who_is_bharat()

