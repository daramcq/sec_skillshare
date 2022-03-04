import requests

# This is a function to get the starships
def get_starships(page=1):
    starships = []
    remaining = True
    while remaining:
        resp = requests.get('https://swapi.dev/api/starships/?page={}'.format(page))
        js = resp.json()
        for result in js['results']:
            starships.append(result['name'])
        if js['next']:
            page += 1
        else:
            remaining = False
    # This will return the result to the caller of this function
    return starships


# This runs the code in the block when the file is executed by Python.
if __name__ == '__main__':
    print(get_starships())
