# 첫번째 숫자를 넣으세요 1
# 두번째 숫자를 넣으세요 2
# 숫자의 합은 3

a = int(input("첫번째 숫자를 넣으세요"))
b = int(input("두번째 숫자를 넣으세요"))
print("숫자의합은" + str(a + b))
print("숫자의합은",str(a + b))           # 뛰어쓰기들어감
print("숫자의합은 {}".format(a + b))     # str 캐스팅 필요없다
