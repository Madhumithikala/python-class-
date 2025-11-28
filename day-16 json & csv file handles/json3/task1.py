#write a python script to read emp.json file and
#print no of male employees
#print no of female employees

import json
""" with open('emp.json','r') as fp:
    employees=json.load(fp) """

fp=open('emp.json','r')
data=json.load(fp)


print("no of employees:",len(data))

male_count=0
female_count=0
for emp in data:
    if emp['gender']=='Male':
        male_count = male_count + 1
    elif emp['gender']=='Female':
        female_count = female_count + 1
        
print("No of Male Employees:",male_count)
print("No of Female Employees:",female_count)