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

        for i in range(1,11):
            topList.append(getGames['list_{}'.format(i)])


        return topList


#a = TrendingSales.getTopTen()

#for games in a:
    #print(games[0], games[1], games[2])

#for games in a:
    #print("%s, %s, %s" % games)