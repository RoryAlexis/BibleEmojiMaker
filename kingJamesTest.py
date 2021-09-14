import pornhub


allowableWords = set()
with open("the-king-james-bible.txt", "r") as f:
    allTheLines = f.readlines()
    for line in allTheLines:
        words = line.split(" ")
        for word in words:
            allowableWords.add(word)

def getKeyWords():
    print("type all your keywords seperated by a space")
    keywords = input().split(" ")

    hasBadWords = False
    badWords = []
    for keyword in keywords:
        if keyword not in allowableWords:
            hasBadWords = True
            badWords.append(keyword)

    if hasBadWords:
        print("{}! That word is not approved by Jesus! Try again \n\n\n\n\n".format(", ".join(badWords).title()))   
        keywords = getKeyWords()
    
    return keywords
#client = pornhub.PornHub("5.135.164.72", 3128, search_keywords)
#With proxy, given a Proxy IP and Port. For the countries with restricted access like Turkey, etc.
search_keywords = getKeyWords()
print(search_keywords)
client = pornhub.PornHub(search_keywords)
   
for video in client.getVideos(quantity=10):
    print(video["name"])
    print(video["url"])
    print()