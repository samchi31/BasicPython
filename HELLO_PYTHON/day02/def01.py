from dask.array.numpy_compat import divide
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b;
def divide(a,b):
    return a/b;

sum = add(5,4)
min = minus(5,4)

print("sum", sum)
print("minus",min)
print("multiply", multiply(5, 4))
print("divide", divide(5,4))