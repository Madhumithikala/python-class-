""" print(10/5)
print(10/0)
print(10/1)
print('GE')                   #risky code
 """

""" 
program terminate abnormally 
"""


print(10/5)
try:                                #risky code
    print(10/0)
except:
    print("can't divide by zero")
print(10/1)
print("GE")