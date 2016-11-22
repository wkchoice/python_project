'''
Created on 2016. 11. 22.

@author: ewankch
'''
print("Hello")
s = "World"

# data type : tuple
t1 = ()
t2 = (1)
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ("a","b",("ab","cd"))
print(t2)
print(t3)
print(t5)

def add(i,j):
    return i+j

print(add(3,4))

t11 = (1,2,"a","b")
print(t11)
print(t11[2])
print(t11[1:])
