from bs4 import BeautifulSoup
import requests

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


#attempt to scrape using requests only, unfortunately it needs a javascript initiation

class AllKeySales:
    def KeySales(game):
        """
        myOptions = ChromeOptions()
        myOptions.add_argument('start-maximized')
        myOptions.add_argument('--lang=en-GB')
        myOptions.add_experimental_option('detach', True)

        driver = Chrome(options=myOptions)
        driver.set_window_size(1920, 1080)
        """
        
        search_url = f'https://www.allkeyshop.com/blog/catalogue/search-{game}'

        page = requests.get(search_url)
        soup = BeautifulSoup(page.text, 'html.parser')

        a_href = soup.find("a",{"class":"search-results-row-link"}).get("href")
        str(a_href)

        nextpage = requests.get(a_href)
        nextsoup = BeautifulSoup(nextpage.text, 'html.parser')

        
        info = nextsoup.find(class_="offers-table x-offers")

        topList = []

        buyerName = [games.get_text() for games in info.find_all(class_="x-offer-merchant-name offers-merchant-name")]
        buyerPrice = [games.get_text() for games in info.find_all(class_="x-offer-buy-btn-in-stock")]
        del buyerPrice[2::2]

        for i in range(len(buyerName)-1):
            topList.append(buyerName[i])
            i += 1
            topList.append(buyerPrice[i])

        getGames = {'list_{}'.format(i): e for i, e in enumerate(zip(*[iter(topList)]*2), 1)}

        #print(nextsoup.prettify)
        print(a_href)
        

        #return info


AllKeySales.KeySales("astroneer")
#print(AllKeySales.KeySales("astroneer"))