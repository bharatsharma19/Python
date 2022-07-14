# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
# print("Pattern printing")
# num = int(input("Enter num how many rows you want : "))
# print("Enter 1 or 0")
# bool_val = input("1 for True value or 0 for False : ")
# if bool_val=="1":
#     for i in range(0,num+1):
#         print("*"*i)
#
# if bool_val=="0":
#     for i in range(num,0,-1):
#         print("*"* i)


a = int(input("please add number of line you want to print"))
b = bool(int(input("please add 0 for False")))


def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a, b)
