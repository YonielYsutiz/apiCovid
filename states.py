import requests 
import json

if __name__ == '__main__':
    url = 'https://api.covidtracking.com/v1/states/info.json'
    response = requests.get(url)
    print(response.url)

    if response.status_code == 200:
        response_states = response.json()

        cont=0
        if len(response_states) > 0:
            for states in response_states:
                if 1 in states:
                    cont += 1
                else: print("Aqui!!!",states)
            