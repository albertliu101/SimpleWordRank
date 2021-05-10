import requests
import re
from bs4 import BeautifulSoup
def getGenericText(website):
    currReq = requests.get(website)
    soup = BeautifulSoup(currReq.content,'html.parser')
    searchList = ['h1','h2','p','div']
    retDict = {}
    for searchType in searchList:
        currSearch = soup.find_all(searchType)
        textList = []
        for entry in currSearch:
            textList.append(entry.text)
        retDict[searchType] = textList
    return retDict