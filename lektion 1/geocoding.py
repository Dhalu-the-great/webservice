import requests

def geocode(adresse):
    url="https://nominatim.openstreetmap.org/search"

    query_params= {
        "q" : adresse,
        "format": "json"
    }


    header = {
        "User-Agent": "RIOT Games Webclient V9.17"
    }

    r = requests.get(url,params=query_params,headers=header)

    if r.status_code==200:
        data=r.json()
        return data

    else:
        print(f"Fehler!!")


resultat = geocode("Hofackerstrasse 30 , 4132 Muttenz, Schweiz")
print(resultat)