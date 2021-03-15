import requests
from PIL import Image
import string
import json

reponse = requests.get("https://covid19.mathdro.id/api")
info = reponse
info = json.loads(info.text)
confirmados = info["confirmed"]["value"]
recuperado = info["recovered"]["value"]
mortos = info["deaths"]["value"]
data = info["lastUpdate"]
print(confirmados, mortos, recuperado, data)



