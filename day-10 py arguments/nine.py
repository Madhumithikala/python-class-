def get_bal(name,acc_bal):
    min_bal=500
    return name,acc_bal-min_bal
bal1=get_bal("Rahul",5000)
print(bal1)  #4500
bal2=get_bal("Madhu",15000)
print(bal2)  #14500

