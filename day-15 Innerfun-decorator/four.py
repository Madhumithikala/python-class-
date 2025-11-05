def  calc():
    print("outer function started.")
    def add():
        print("Addition done.")    
    def multi():
        print("Multiplication done.")
    return  add, multi
inner=calc()
print(type(inner))
inner[0]()
inner[1]()  
