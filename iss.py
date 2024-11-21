import requests
import json

class SpaceInfo:

    def position(self):
        donnees_brutes = requests.get("http://api.open-notify.org/iss-now.json")
        text = donnees_brutes.text

        data = json.loads(text)

        return data

    def recensement(self):
        donnees_brutes = requests.get("http://api.open-notify.org/astros.json")
        text = donnees_brutes.text

        data = json.loads(text)
        return data

test_api = SpaceInfo()

print(test_api.position()['iss_position'])
print(test_api.position()['timestamp'])

print('\n')

test2_api = test_api.recensement()
dans_iss = []
population = 0
people = test2_api['people']


for quidam in people:
    if quidam['craft'] == "ISS":
        dans_iss.append(quidam['name'])
        population += 1

print(f"Il y a {population} personnes dans l'ISS. Voici leurs noms :")
for astronaute in dans_iss:
    print(astronaute)
