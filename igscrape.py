from bs4 import BeautifulSoup
import requests

class TrendingSales:

    def getTopTwenty():
        url = "https://www.instant-gaming.com/en/search/"

        page = requests.get(url)
        doc = BeautifulSoup(page.text, "html.parser")

        info = doc.find(class_="search listing-games")

        gametext = [games.get_text() for games in info.find_all(class_=["discount","title", "price"])]

        d = {'list_{}'.format(i): e for i, e in enumerate(zip(*[iter(gametext)]*3), 1)}

        for i in range(1,20):
            print(d['list_{}'.format(i)])

TrendingSales.getTopTwenty()