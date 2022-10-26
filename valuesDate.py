import requests
import json

if __name__ == '__main__':
    url ='https://api.covidtracking.com/v1/us/20200115.json'
    response = requests.get(url)
    print("url !!!", response.url)

    if response.status_code == 200:
        response_json = response.json()
        print(response_json)