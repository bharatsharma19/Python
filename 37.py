class Employee:
    no_of_leaves = 8
    pass

Bharat = Employee()
Vivek = Employee()

Bharat.Name = "Bharat"
Vivek.Name = "Vivek"
Bharat.Salary = 18798564
Vivek.Salary = 15987651
Bharat.Role = "CEO"
Vivek.Role = "Software Engineer"

#print(Bharat.Name,Bharat.Salary,Bharat.Role)
#print(Vivek.Name,Vivek.Salary,Vivek.Role)
#print(Vivek.no_of_leaves)
print(Bharat.__dict__)
print(Vivek.__dict__)
Vivek.no_of_leaves = 9
print(Employee.no_of_leaves)
print(Employee.__dict__)
