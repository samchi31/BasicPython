# 홀/ 짝을 넣으세요
# 같으면 이김 다르면 짐
import random

rnd = random.random()
me = input("홀/짝 입력:")
com = ""
if rnd > 0.5 :
    com = "짝"
else:
    com = "홀"

# print(rnd,com)
if me == com:
    print("이김")
else :
    print("짐")
