# 구구단 출력할 단 수를 입력

dan = int(text("출력할 단 수 입력 : "))

for i in range(1,10):
    print("{} * {} = {}".format(i,dan,i*dan))