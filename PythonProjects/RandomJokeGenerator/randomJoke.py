import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
joke = response.json()        # This returns json object

setup = joke['setup']         # fetch the setup using key 'setup'
punchline = joke['punchline'] # fetch the punch line using key

print(setup)
print(punchline)


'''✨ Extensions you can try:

- Fetch 10 random jokes instead of 1 → use https: // official-joke-api.appspot.com/random_ten.

- Allow user to choose a category(general, programming, knock-knock).

- Save jokes to a file(jokes.txt).
'''