#create dict


d1={}
emp={
    'eid':101,
    'ename':'madhu',
    'esal':55000
}

#read dict
print(d1)
print(emp)

print(emp['eid'])
print(emp['ename'])
print(emp['esal'])


#update dict 
emp['ename']='rahul'
emp['esal']=67000


#delete dict
del emp['esal']
print(emp)