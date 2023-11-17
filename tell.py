import requests

def get_joke():
    url = f'https://v2.jokeapi.dev/joke/any'
    response = requests.get(url)
    
    results = response.json()
    if 'delivery' in results.keys():
        return results['setup'] + results['delivery']
    else: return results['joke']

def get_pickup():
    url = f'https://vinuxd.vercel.app/api/pickup'
    response = requests.get(url)
    
    results = response.json()
    return results['pickup']