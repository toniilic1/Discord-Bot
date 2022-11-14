from bs4 import BeautifulSoup
import requests

class TrendingSales:

    def getTopTen():
        global url
        global topList

        url = "https://www.instant-gaming.com/en/search/" #test for correct url

        page = requests.get(url)
        doc = BeautifulSoup(page.text, "html.parser")

        info = doc.find(class_="search listing-games") #test if divs on url

        gametext = [games.get_text() for games in info.find_all(class_=["discount","title", "price"])]

        getGames = {'list_{}'.format(i): e for i, e in enumerate(zip(*[iter(gametext)]*3), 1)}
    
        topList = []

        for i in range(1,11):
            topList.append(getGames['list_{}'.format(i)]) #test for 3 elements in every list


        return topList


#print(TrendingSales.getTopTen())