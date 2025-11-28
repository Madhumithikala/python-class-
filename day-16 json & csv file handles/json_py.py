import json
emp_str='''
[
    {"eid":101,"ename":"Rahul","avail":True,"grade":None},
    {"eid":102,"ename":"Sonia","avail":False,"grade":None},
    {"eid":103,"ename":"Priyanka","avail":True,"grade":None},
    {"eid":104,"ename":"Modi","avail":False,"grade":None},
    {"eid":105,"ename":"Amith","avail":True,"grade":None}
]'''

employees=json.loads(emp_str)
print(employees)