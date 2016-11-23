'''
Created on 2016. 11. 23.

@author: ewankch
'''
# function is Objective clearly. function can be a variable. or assigned a variable
def foo(a,b):
    print a, b

x = foo
x(1,2)

print foo
print x

# argument of function can  be a function clearly
def foo1(f,a):
    return f(a)

def square(x):
    return x*x

y =foo1(square,3)
print y

def add10(x):
    return x+10

y = foo1(add10, 5)
print y

# result of function can be returned with another Function
def foo2(x):
    def bar(k):
        return x+k
    return bar 

f = foo2(5)
# print f
print f(2)

f1 = foo2(30)
print f1(9)

