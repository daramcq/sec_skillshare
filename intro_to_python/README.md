# Introduction to Python
Now that we know how to do basic package management, let's go over some basic Python. Let's keep using the virtual environment we created in the last example.

## Goal
We're going to use the `requests` package to query a HTTP API for information about the Star Wars movies and go over basic Python - control flow and data structures.

## Checking the basic usage
With your virtual environment active, run `python`. You should see that something like this:
```
Python 3.8.2 (default, Nov  4 2020, 21:23:28)
[Clang 12.0.0 (clang-1200.0.32.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The `>>>` are where you can enter code.

### Requesting a page
To start using a package, you need to import it:
```
>>> import requests
```
Let's test that we can access the API.
```
>>> requests.get('https://swapi.dev/api/starships/9')
<Response [200]>
```
So we are getting a response object back. Let's capture that in a variable:
```
>>> resp = requests.get('https://swapi.dev/api/starships/9')
```
We can check the type of the object like this:
```
>>> type(resp)
<class 'requests.models.Response'>
```
This is a response object. 

### Using a `dict`
We know that the API returns JSON and we can access this using the `response.json` method.
```
>>> obj = resp.json()
>>> obj
{'name': 'Death Star', 'model': 'DS-1 Orbital Battle Station', 'manufacturer': 'Imperial Department of Military Research, Sienar Fleet Systems', 'cost_in_credits': '1000000000000', 'length': '120000', 'max_atmosphering_speed': 'n/a', 'crew': '342,953', 'passengers': '843,342', 'cargo_capacity': '1000000000000', 'consumables': '3 years', 'hyperdrive_rating': '4.0', 'MGLT': '10', 'starship_class': 'Deep Space Mobile Battlestation', 'pilots': [], 'films': ['https://swapi.dev/api/films/1/'], 'created': '2014-12-10T16:36:50.509000Z', 'edited': '2014-12-20T21:26:24.783000Z', 'url': 'https://swapi.dev/api/starships/9/'}
>>> type(obj)
<class 'dict'>
```
The `dict` class is a 'dictionary', which is a hash (mapping of keys to values). It's a very useful data structure. We can access the values in a number of ways.
```
>>> obj['name']
'Death Star'
```
We can look at all the keys by iterating through them.
```
>>> obj.keys()
dict_keys(['name', 'model', 'manufacturer', 'cost_in_credits', 'length', 'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity', 'consumables', 'hyperdrive_rating', 'MGLT', 'starship_class', 'pilots', 'films', 'created', 'edited', 'url'])
```

### Using a `list`
To flatten this out, we can do:
```
>>> [k for k in obj.keys()]
['name', 'model', 'manufacturer', 'cost_in_credits', 'length', 'max_atmosphering_speed', 'crew', 'passengers', 'cargo_capacity', 'consumables', 'hyperdrive_rating', 'MGLT', 'starship_class', 'pilots', 'films', 'created', 'edited', 'url']
>>> type([k for k in obj.keys()])
<class 'list'>
```
This is a list, the other most important datastructure.

## Expanding on this
We should probably get writing code in a file so that we don't lose our work. Create a new file called `swapi.py` and add the following code into it:

```python
import requests

# This is a function to get the starships
def get_starships():
    resp = requests.get('https://swapi.dev/api/starships/')
    # This will return the result to the caller of this function
    return resp.json()
    
    
# This runs the code in the block when the file is executed by Python.
if __name__ == '__main__':
    print(get_starships())
```
You can run this using `python swapi.py`.

### Challenges
Let's see if we can get a list of _all_ the Star Wars spaceships. Note that if we request `https://swapi.dev/api/starships/`, the response JSON has a key `'next'`. This will give us a value like `'https://swapi.dev/api/starships/?page=2'`.
