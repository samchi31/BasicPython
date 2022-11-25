def gugudan():
    for i in range(9,6,-1):
        for j in range(1,10):
            print("{} * {} = {}".format(i, j, i*j))
    for j in range(1,10):
            print("2 * {} = {}".format(j, 2*j))
print(gugudan())

def gugudan1(dan):
    for i in range(1,10):
        print("{} * {} = {}".format(dan,i,dan*i))