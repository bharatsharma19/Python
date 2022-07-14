f1 = open("bharat.txt")

try:
    f = open("does.txt")

except EOFError as e:
    print("Print EOF error occured!", e)

except IOError as e:
    print("Print IO error occured!", e)

else:
    print("This will run if except is not running\n")

finally:
    print("Run this anyway...")
    f.close()
    f1.close()

print("Important Stuff")
