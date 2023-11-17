import requests
API_KEY = open('assert/API_KEY').read()
SEARCH_ENGINE_ID = open('assert/SEARCH_ENGINE_ID').read()
query = 'Vietnam'

url = 'https://www.googleapis.com/customsearch/v1'
params = {'q': query, 
          'key': API_KEY, 
          'cx': SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)
results = response.json()
print(results)