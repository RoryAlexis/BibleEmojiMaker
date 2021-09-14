import json

word_to_emoji = {}
with open("emojiDictionary.json", encoding="utf-8") as f:
    word_to_emoji = json.load(f)
punctuation = ".?,!():;"

allTheLines = []
with open("the-king-james-bible.txt", "r") as f:
    allTheLines = f.readlines()

with open("myEmojiBible.txt", "w", encoding="utf-8") as f:
    for line in allTheLines:
        f.write("\n")
        line = line.strip()
        for word in line.split(" "):
            punctuationMark = None
            try:
                if word[-1] in punctuation:
                    punctuationMark = word[-1]
            except:
                pass
            try:
                emoji = word_to_emoji[word]
                f.write(emoji + " ")
            except KeyError:
                f.write(word + " ")
            if punctuationMark is not None:
                    f.write(punctuationMark)