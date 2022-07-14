class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.Name = aname
        self.Salary = asalary
        self.Role = arole

    def printdetails(self):
        return f"Name is {self.Name}, Salary is {self.Salary} and Role is {self.Role}"

Bharat = Employee("Bharat",129887654,"CEO")
Vivek = Employee("Vivek",1257421,"Software Er.")

#Bharat.Name = "Bharat"
#Vivek.Name = "Vivek"
#Bharat.Salary = 18798564
#ivek.Salary = 15987651
#Bharat.Role = "CEO"
#Vivek.Role = "Software Engineer"

print(Bharat.printdetails())
print(Vivek.printdetails())

