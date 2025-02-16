import requests

url = 'http://abcdefg12345.onion/upload'  # your .onion address
files = {'file': open('image.jpg', 'rb')}

response = requests.post(url, files=files)
print(response.text)