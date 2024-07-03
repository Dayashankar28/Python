import json, requests
url = 'https://fakestoreapi.com/users'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    user_data_list = [] # to append user details

    for i in data:

        user_data = {
            "id" : i["id"],
            "username": i["username"],
            "Mobile" : i["phone"]
        }
        if user_data["id"] <= 6:
            user_data_list.append(user_data)
        else:
             print("User not found")
else:
    print("No connection")

print(len(user_data_list))

with open("example.txt", "w") as f1:
    f1.write(json.dumps(user_data_list))
