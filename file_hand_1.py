# import json
# data = ""
# with open("dummy_data.txt", "r", encoding="utf8") as f1:
#    data = f1.read()

# def get_description(d):
#    return d["description", "teams_url"]

# description =  list(map(get_description, json.loads(data)))
# print((description))

# #//////////////////////////////////////////

import json, requests, wget
data = ""
ur = 'https://api.github.com/users/timmywheels/repos?ref=codesnippet.io'

response = requests.get(url)
data = response.json()
print(type(data))

def get_users(d):
   return d["teams_url"]

users = list(map(get_users, json.loads(data)))
print(users)