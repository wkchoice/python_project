'''
Created on 2016. 11. 22.

@author: ewankch
'''
def sum_many(*args):
    s = 0
    for i in args:
        s += i
    return s
    
a = sum_many(1,2,3,4,10)
print a