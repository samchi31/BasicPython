from _cffi_backend import typeof
def addminmuldiv(a,b):
    return a+b,a-b,a*b,a/b

print(addminmuldiv(5, 4))

print(type(addminmuldiv(5, 4)))