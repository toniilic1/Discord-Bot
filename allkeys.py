from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

game = input("Enter game name: ")

myOptions = ChromeOptions()
myOptions.add_argument('start-maximized')
myOptions.add_argument('--lang=en-GB')
myOptions.add_experimental_option('detach', True)

driver = Chrome(options=myOptions)
driver.get(f'https://www.allkeyshop.com/blog/catalogue/search-{game}')

searchgame = driver.find_element(By.CLASS_NAME, "search-results-row-link")
searchgame.click()

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

info = soup.find(class_="offers-table x-offers")

topList = []

buyerName = [games.get_text() for games in info.find_all(class_="x-offer-merchant-name offers-merchant-name")]
buyerPrice = [games.get_text() for games in info.find_all(class_="x-offer-buy-btn-in-stock")]
del buyerPrice[2::2]

for i in range(len(buyerName)-1):
    topList.append(buyerName[i])
    i += 1
    topList.append(buyerPrice[i])

getGames = {'list_{}'.format(i): e for i, e in enumerate(zip(*[iter(topList)]*2), 1)}

print(getGames)