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

# Write a program to print number of male and female employees
male_count=0
female_count=0
bi_gender=0

for emp in employees:
    if emp['gender']=='Male':
        male_count=male_count+1
    elif emp["gender"]=='Female':
        female_count=female_count+1
    else:
        bi_gender+=1


print("No of male employees:",male_count)
print("No of female employees:",female_count)
print("No of Bi-gender employees:",bi_gender)