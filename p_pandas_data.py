import requests, pandas as pd

url = 'https://api.escuelajs.co/api/v1/products'

# Send GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract image URLs from the response data
    image_urls = []
    for product in data:
        if 'images' in product:
            image_urls.append(product['images'])

    # Print the extracted image URLs
    for url in image_urls:
        print(url)
else:
    print(f"Failed to retrieve data: {response.status_code}")



df = pd.DataFrame(image_urls, columns=['Image URL'])
excel_filename = 'product_images.xlsx'
df.to_excel(excel_filename, index=False)
