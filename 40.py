class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.Name = aname
        self.Salary = asalary
        self.Role = arole

    def printdetails(self):
        return f"Name is {self.Name}, Salary is {self.Salary} and Role is {self.Role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
         # params = string.split("-")
         # print(params)
         # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

Bharat = Employee("Bharat",1,"CEO")
Vivek = Employee("Vivek",1,"Software Er.")
Shivam = Employee.from_str("Shivam-1-Client")

print(Shivam.Salary)

