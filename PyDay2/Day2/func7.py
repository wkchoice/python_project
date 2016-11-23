'''
Created on 2016. 11. 22.

@author: ewankch
'''
a = 11

def var_test():
    global a
    a += 1

var_test()
print a