"""
Iterable - __iter__ () or __getitem__()
Iterator - __next__()
Iteration - 
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
#print(g)
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())

#for i in g:
    #print(i)

b = "Bharat"
print(iter(b))

for c in b:
    print(c)
    