'''
Created on 2016. 11. 23.

@author: ewankch
'''
t = [1,2,3] # Mutable, call by reference

def test(a):
    a += [4,5,6]
    print a
    
test(t)
print t

t1 = {1:'a'}
def test1(a):
    a[2] = 'b'

test1(t1)
print t1