# 가위바위보
from random import random

me = text("가위 바위 보 입력 : ");

coms = ["가위", "바위", "보"]

com = coms[int(random()*3)]
print("com",com)
if com == me :
    print("무승부")
elif (com == "가위" and me == "바위") or (com == "바위" and me == "보") or (com == "보" and me == "가위"):
    print("me 이김")
else:
    print("com 이김")