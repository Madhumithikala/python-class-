#how to invoke inner functions from outside?
def outer():
    print("outer function executed.")
    def inner():
        print("inner function executed.")
    return inner
inn=outer()
print(inn) 
inn()
inn()

