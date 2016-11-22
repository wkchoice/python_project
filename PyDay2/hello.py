# coding: utf-8
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
t22 = (3,4)
print(t11)
print(t11[2])
print(t11[1:])

print(t11 + t22)
#
dic = {"name":"home", "phone":"010-1234-5678", "birth":"080409"}
print(dic)

#list
x = [1, 2]
y = x
y.append(4)
print(x)
 
a, b = "python", "life"
print(a,b)

if [1,2,3]:
    print "True"
else:
    print "False"
    

# substitude
a, b = b, a
print(a,b)
print(id(a)) # address of variable(a)

money = 5000
if money:
    print "택시"
else:
    print "도보"
    

pocket = ["paper", "handphone", "money"]
watch = 1
if "money" in pocket:
    print "모범 택시"
elif watch:
    print "자가용"
else:
    print "도보"
    

t = 0
while t < 10:
    t += 1
    print "나무 %d번 베었습니다"%t
    if t == 10:
        print "나무를 모두 베었습니다"

print "for "
marks = [10,22,33,66, 88, 99, 100]
for mark in marks:
    print mark,"점은 ",
    if mark >= 60:
        print "합격"
    else:
        print "불합격"

print "while"
t = 0
while  t < len(marks):
    print t,"번째 ", marks[t]
    t += 1
    
ra = range(1,11)
print ra

sum = 0
for i in range(1,11):
    sum += i
print sum




