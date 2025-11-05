#positional argument
def calc(a,b):
    print(a-b)
calc(100,200) #-100
calc(200,100) #100


# change position argument(this is positional argument)
def calc(a,b):
    print(a-b)
calc(a=100,b=200) #-100
calc(b=200,a=100) #-100
