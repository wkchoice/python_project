#lotto.py

'''
Created on 2016. 11. 22.

@author: ewankch
'''

import random

#lotto1
y = set()
while len(y) < 6:
    y.add(random.randint(1,45))
#     print i, y
print sorted(y)
 
#lotto1 
balls = range(1,46)
random.shuffle(balls)
myballs = balls[0:6]
# print balls
print sorted(myballs)

#lotto2
for i in range(5):
    print sorted(random.sample(range(1,46), 6))

# lotto3
cnt = 0
s = 0
while cnt < 5:
    lotto = sorted(random.sample(range(1,46), 6))
    s = sum(lotto)
    if 100 <= s <= 170:
        print(lotto, "sum= ", s)
        cnt += 1
