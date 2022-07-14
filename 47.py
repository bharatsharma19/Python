class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance Variable in class A"

class B(A):
    classvar2 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "Instance Variable in class B"
        print(super().classvar1)

a = A()
b = B()

print(b.classvar1)
