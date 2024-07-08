import json, requests

def add(a, b):
    print(f' sum of {a} + {b} is {a+b}')
    
def sub(a, b):
    return a - b


def welcome(name):
    print(f'Welcome.... {name}!!!!!!')

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

def get_data(url):
    response = requests.get(url)
    return response.json()