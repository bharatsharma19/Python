class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@bharatsharma.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@bharatsharma.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


vivek_sharma = Employee("Vivek", "Sharma")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(vivek_sharma.email)

vivek_sharma.fname = "US"

print(vivek_sharma.email)
vivek_sharma.email = "this.that@codewithharry.com"
print(vivek_sharma.fname)

del vivek_sharma.email
print(vivek_sharma.email)
vivek_sharma.email = "Harry.Perry@codewithharry.com"
print(vivek_sharma.email)

