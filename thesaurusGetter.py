from bs4 import BeautifulSoup
import requests
import urllib

def getSynonyms(myWord):
    pageBaseUrl = "https://www.thesaurus.com/browse/"
    
    try:
        myWordURL = urllib.parse.quote(myWord)
        listOfSynonyms = []
        page = requests.get(pageBaseUrl + myWordURL)
        soup = BeautifulSoup(page.content, "html.parser")
        mainSectionTag = soup.find("section", {"class": "MainContentContainer"})
        listOfSynonymsTag = mainSectionTag.find_all("ul")[1]
        synonymsHeaderTag = listOfSynonymsTag.previous_sibling
        assert "Synonyms for" in synonymsHeaderTag.get_text()
        allTheSynonymsAnchorTags = listOfSynonymsTag.find_all("a")
        for synonymTag in allTheSynonymsAnchorTags:
            listOfSynonyms.append(synonymTag.get_text().strip())
    except Exception as e:
        print("Error with finding synonyms for {}.  Error: {}".format(myWord, str(e)))
    return listOfSynonyms

