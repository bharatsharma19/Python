class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.Name = aname
        self.Salary = asalary
        self.Role = arole

    def printdetails(self):
        return f"Name is {self.Name}, Salary is {self.Salary} and Role is {self.Role}"

    classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

Bharat = Employee("Bharat",1,"CEO")
Vivek = Employee("Vivek",1,"Software Er.")

Bharat.change_leaves(64)
Employee.no_of_leaves = 36
print(Bharat.no_of_leaves)
print(Employee.no_of_leaves)
