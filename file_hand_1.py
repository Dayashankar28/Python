# #//////////////////////////////////////////
import requests, json, wget

# API URL
url = 'https://fakestoreapi.com/users'

# Send GET request
response = requests.get(url)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    
    # List to store dictionaries of id, username, and phone
    user_data_list = []
    
    # Iterate over each user and extract id, username, and phone
    for user in data:
        user_data = {
            "id": user['id'],
            "username": user['username'],
            "phone": user['phone']
        }
        if user_data['id'] < 6:
            user_data_list.append(user_data)
        else:
            break
    
    # Print the list of dictionaries
    for user_data in user_data_list:
        print(user_data)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
# with open("example.txt", "w") as f1:
#     f1.write(json.dumps(user_data_list))

