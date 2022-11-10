from bs4 import BeautifulSoup
import requests

class TrendingSales:

    def getTopTen():
        url = "https://store.steampowered.com/explore/new/" #test for correct url

        page = requests.get(url)
        doc = BeautifulSoup(page.text, "html.parser")

        info = doc.find(class_="home_tabs_content")

        gamename = [games.get_text() for games in info.find_all(class_="tab_item_name")]
        gameprice = [games.get_text() for games in info.find_all(class_="discount_final_price")]

        gametext = []

        for i in range(1,11):
            gametext.extend([gamename[i], gameprice[i]])

        getGames = {'list_{}'.format(i): e for i, e in enumerate(zip(*[iter(gametext)]*2), 1)}

    
        topList = []

        for i in range(1,11):
            topList.append(getGames['list_{}'.format(i)]) #test for 3 elements in every list

        return topList