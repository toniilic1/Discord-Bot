from bs4 import BeautifulSoup
import requests

class TrendingSales:

    def getTopTen():
        url = "https://www.instant-gaming.com/en/search/"

        page = requests.get(url)
        doc = BeautifulSoup(page.text, "html.parser")

        info = doc.find(class_="search listing-games")

        gametext = [games.get_text() for games in info.find_all(class_=["discount","title", "price"])]

        getGames = {'list_{}'.format(i): e for i, e in enumerate(zip(*[iter(gametext)]*3), 1)}
    
        topList = []

        for i in range(1,20):
            topList.append(getGames['list_{}'.format(i)])
        

        """
        for i in range (0, 19):
            x = 0
            for x in range(0, 3):
                yield topList[i][x]
        """

        
        return topList

#a = str(TrendingSales.getTopTwenty())
#print(a)