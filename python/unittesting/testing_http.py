import unittest
import requests
import responses

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


class TestGetStarships(unittest.TestCase):
    @responses.activate
    def test_get_starships(self):
        responses.add(responses.GET,
                      'https://swapi.dev/api/starships/?page=1',
                      json={
                          'next': None,
                          'results': [{'name': 'sillyship'},
                                      {'name': 'milleniumfailcon'}]
                      })
            
        self.assertEqual(['sillyship', 'milleniumfailcon'],
                         get_starships(1))

    @responses.activate
    def test_get_starships_empty_response(self):
        responses.add(responses.GET,
                      'https://swapi.dev/api/starships/?page=1',
                      json={
                          'next': None,
                          'results': []
                      })
        self.assertEqual([], get_starships(1))
        # We can also confirm the API call is made
        self.assertEqual(1, len(responses.calls))


if __name__ == '__main__':
    unittest.main()
