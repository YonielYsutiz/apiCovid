import requests
import json

if __name__ == '__main__':
    url = 'https://api.covidtracking.com/v1/us/current.json'
    response = requests.get(url)
    print(response.url)

    if response.status_code == 200:
        response_current = response.json()
        print(response_current)