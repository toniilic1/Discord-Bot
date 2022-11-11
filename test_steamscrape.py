from steamscrape import *

SteamTrends.getTopTen()

from steamscrape import url, topList

class TestSteam:
    def test_SteamURL(self):
        assert url == 'https://store.steampowered.com/explore/new/', "URL is incorrect"

    def test_SteamLenght(self):
        assert len(topList) == 10, "Incorrent number of lists"

    def test_SteamElNum(self):
        for i in range(0, 10):
            assert len(topList[i]) == 2, "List does not contain 3 elemenets"
