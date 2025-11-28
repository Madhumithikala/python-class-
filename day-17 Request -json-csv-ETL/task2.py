import requests,json
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()
fp=open('users.json','w')
json.dump(users,fp,)
print('new file created')
fp.close()