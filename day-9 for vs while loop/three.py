employees=[{"eid":1,"ename":"Gris","email":"gpimlock0@sciencedaily.com","gender":"Male"},
{"eid":2,"ename":"Jennifer","email":"jbenian1@amazon.co.jp","gender":"Polygender"},
{"eid":3,"ename":"Stephannie","email":"srarity2@virginia.edu","gender":"Female"},
{"eid":4,"ename":"Emalee","email":"ebunney3@elpais.com","gender":"Female"},
{"eid":5,"ename":"Valaria","email":"vbrasener4@uiuc.edu","gender":"Female"},
{"eid":6,"ename":"Nolan","email":"nbellin5@who.int","gender":"Male"},
{"eid":7,"ename":"Bonni","email":"bbunnell6@github.com","gender":"Female"},
{"eid":8,"ename":"Trstram","email":"treinisch7@acquirethisname.com","gender":"Male"},
{"eid":9,"ename":"Dorette","email":"dneame8@ustream.tv","gender":"Female"},
{"eid":10,"ename":"Richmond","email":"rdrain9@cocolog-nifty.com","gender":"Male"},
{"eid":11,"ename":"Donny","email":"dlechmerea@de.vu","gender":"Female"},
{"eid":12,"ename":"Rogers","email":"rbachellierb@google.es","gender":"Male"},
{"eid":13,"ename":"Zenia","email":"zmichelc@reverbnation.com","gender":"Female"},
{"eid":14,"ename":"Brear","email":"bneamed@youtube.com","gender":"Female"},
{"eid":15,"ename":"Kimmi","email":"klukovice@guardian.co.uk","gender":"Female"}
]
""" for emp in employees: """
"""     print(emp) """

# print all employee names
#using for and while loop

#for loop
""" for emp in employees: """
"""     print(emp["ename"]) """

#while loop
""" i=0; """
""" while i<=len(employees)-1: """
"""     print(employees[i]['ename']) """
"""     i=i+1 """

""" for emp in employees: """
"""     print(emp['email']) """

for emp in employees:
    print(emp['eid'])