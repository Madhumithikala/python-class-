""" def outer():
    print("outer function executed.")
    def inner():
        print("inner function executed.")
outer()
inner() """


def calc():
    print("Calculation complete.")
    def add():
        print("Addition done.")    
    def multiply():
        print("Multiplication done.")
    return 100 
value = calc()
print(value)

    