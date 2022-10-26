import requests
import json

if __name__ == '__main__':
    url ='https://api.covidtracking.com/v1/us/daily.json'
    response = requests.get(url)
    print("url !!!", response.url)

    if response.status_code == 200:
        response_json = response.json()

        cont=0
        if len(response_json) > 0:
            for running in response_json:
                if 1 in running:
                    cont += 1
                else: print("Aqui!!!",running)
            
