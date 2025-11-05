def add(a, b):
    def inner():
        print("Inner function")
    return a + b, "madhu",inner
result = add(5, 10)
print( result[0])
print( result[1])
result[2]()
result[2]()
result[2]()
