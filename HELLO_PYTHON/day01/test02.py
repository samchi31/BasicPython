# 첫번째 수를 넣으세요
# 두번째 수를 넣으세요
# 에서 까지 합은 입니다

a = int(input("첫번째 숫자를 넣으세요"))
b = int(input("두번째 숫자를 넣으세요"))
sum=0
for i in range(a,b+1):
    sum += i
print("{}에서{}까지 합은 {}입니다".format(a,b,sum))