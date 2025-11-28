#write py script to read user.csv file 
#and print all usernames 
import csv
with open('user.csv','r') as fp:
    csv_reader=csv.reader(fp)
    # users=list(csv_reader)
    print(type(csv_reader))  #<class '_csv.reader'>
    print(csv_reader)        #<_csv.reader object at 0x0000022C8F1D3B20>

    # for user in users[1:] :
    #     print(user[1],user[2],user[3])

    for user in csv_reader:
        print(user[1],user[2],user[3])