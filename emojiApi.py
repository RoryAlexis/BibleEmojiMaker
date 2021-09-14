import requests
import json

def getEmoji(myWord):
    myAPIkey = "8cb402f051b482a2dac6edef871dfdb2910c8aa2"
    apiURL = "https://emoji-api.com/emojis?search={}&access_key={}".format(myWord, myAPIkey)
    try:
        page = requests.get(apiURL)
        emojiJSON = page.json()[0]
        emojiToReturn = emojiJSON["character"]
        return emojiToReturn
    except Exception as e:
        print("Failed to find emojis through the API for {}.  Error: {}".format(myWord, str(e)))
    

