how to use:
```
from gw2-api-py import API
client = API.v2(apikey="yourSecretKey")
character = client.characters(character="characterID")
print(character) # character is a json object not a string
```

list of all currently implemented endpoints:
```
print(API.endpoints())
```
