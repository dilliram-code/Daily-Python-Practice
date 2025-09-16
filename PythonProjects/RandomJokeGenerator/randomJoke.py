import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
joke = response.json()        # This returns json object

setup = joke['setup']         # fetch the setup using key 'setup'
punchline = joke['punchline'] # fetch the punch line using key

print(setup)
print(punchline)
