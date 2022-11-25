# 로또 생성 (1~45 중복없이 6개)

import random

# lotto = []
# for i in range(1,46) :
#     lotto.append(i)
#
# random.shuffle(lotto)
#
# print(lotto[0:6])
    
    
arr = [1,2,3,4,5,6]
for i in range(1000):
    rnd = int(random.random()*6)
    
    a=arr[0]
    b=arr[rnd]
    arr[0]=b
    arr[rnd]=a
    
print(arr)