import json, requests, pandas as pd
from mymodule import get_data

url = 'https://api.github.com/users/Dayashankar28/repos?ref=codesnippet.io'
response = requests.get(url)
excel_name = url.split('/')[-2] + '_links.xlsx'
txt_file = url.split('/')[-2] + '.txt'
d = response.json()

url_list = []
for links in d:
    if 'downloads_url' in links:
        url_list.append(links['downloads_url'])

print(url_list)

# print(type(d))


# def get_url(i):
#     return i['downloads_url']

# downloads_url_list = list(map(get_url, d))

# print(downloads_url_list)

df = pd.DataFrame({'URL':url_list})
df.to_excel(excel_name, index = False)

with open(txt_file, 'w') as f1:
    f1.write(str(d))