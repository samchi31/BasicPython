# 로또 생성 (1~45 중복없이 6개)

import random
    
arr = []

for i in range(1,46):
    arr.append(i)

for i in range(1000):
    rnd = int(random.random()*45)
    
    a=arr[0]
    b=arr[rnd]
    arr[0]=b
    arr[rnd]=a
    
print(arr)
print(arr[0:6])