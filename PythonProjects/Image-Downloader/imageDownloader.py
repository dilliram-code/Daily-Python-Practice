import requests


url = "https://picsum.photos/200/300"
response = requests.get(url)

with open("image.jpg", "wb") as file:
  file.write(response.content)
  
print("Image downloaded.")