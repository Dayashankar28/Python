import json, requests, pandas as pd
from mymodule import get_data

url = 'https://api.github.com/users/iam-veeramalla/repos?ref=codesnippet.io'

username = url.split('/')[-2] + '_links.xlsx'

d = get_data(url)


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
df.to_excel(username, index = False)