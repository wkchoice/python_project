'''
Created on 2016. 11. 23.

@author: ewankch
'''
t = (1,2,3) # immutable, call by value

def test(a):
    a += (4,5,6)
    print a
    
test(t)
print t

