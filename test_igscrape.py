from igscrape import *

TrendingSales.getTopTen()

from igscrape import url, topList

class TestInstant:
    def test_IgURL(self):
        assert url == 'https://www.instant-gaming.com/en/search/', "URL is incorrect"

    def test_IgLenght(self):
        assert len(topList) == 10, "Incorrent number of lists"

    def test_IgElNum(self):
        for i in range(0, 10):
            assert len(topList[i]) == 3, "List does not contain 3 elemenets"
