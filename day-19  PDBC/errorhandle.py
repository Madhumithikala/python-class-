
# without error handling
a=int(input("Enter First No:"))
b=int(input("Enter Second No:"))
print(a/b)
print("GE")



#with error handling

try:
    a=int(input("Enter First No:"))
    b=int(input("Enter Second No:"))
    print(a/b)
except:
    print("Enter integrity only")
    print("can't  execute")
print('Good Evening')



