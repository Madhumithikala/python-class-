// Writing data to a CSV file
import csv
fp=open('emp.csv','w', newline='')
cw=csv.writer(fp)
cw.writerow(["eid","ename","esal"])
data=[
        (101,'RG',45000),
		(102,'SG',50000),
        (103,'AG',55000),
        (104,'BG',60000)
     ]
cw.writerows(data)
print("successful")
fp.close()
		
		
