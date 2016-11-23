'''
Created on 2016. 11. 22.

@author: ewankch
'''

def sum_mul(choice, *args):
    if choice == "mul":
        result = 1;
        for i in args:
            result *= i
        else:
            result = 0
            for i in args:
                result += i
            return result
        
a = sum_mul("mul", 1,2,3,4)
print a
a = sum_mul("ml", 1,2,3,4)
print a
            