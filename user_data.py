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
        user_data_list.append(user_data)
else:
    print("No connection")

print(len(user_data_list))

with open("example.txt", "w") as f1:
    f1.write(json.dumps(user_data_list))


########### products data #####################

import json, requests, wget

url = 'https://fakestoreapi.com/products'

response = requests.get(url)   # requesting data

def catageory(data):                           #function to select category
    return data["id"] == "jewelery"   #function to select category

if response.status_code == 200:  # checking connection
    data = response.json()       # parsing json

    filtered_data = list(filter(catageory, data))  #filtering catageory

    p_details = []   #empty list to store  required product details
    pid = []         #empty list to store  required id


# loop to itterate through filtered data and get only id, title, price, rating
 
    for i in filtered_data:
        jdata = {
            "ID": i["id"],
            "Title": i['title'],
            "Price": i['price'],
            "Rating":i['rating']['rate']
        }
        p_details.append(jdata)

# loop to itterate through filtered data and get only id

    for i in filtered_data:
        idata = i["id"]
        pid.append(idata)
else:
    print(" --- No Response ---")

print(p_details)
print(f'\n Product ID\'s are {pid}')

# ------------------ products --------------- #

import json, requests
url = 'https://api.escuelajs.co/api/v1/products'
response = requests.get(url)


def scrape(data):
    if data['price'] > 50:
        return data


if response.status_code == 200:
    data = response.json()

    f_data = list(filter(scrape, data))
    print((len(f_data)))

    p_details = []

    for i in f_data:
        d = {
            "Category" : i['category']['name'],
            "Id" : i["id"],
            "Title" : i['title'],
            "Price" : i['price']
        }
        p_details.append(d)
else:
    print(f"Response Status is : {response.status_code}")

print(p_details)




