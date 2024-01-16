from bs4 import BeautifulSoup
import requests
from Entry_bot import Bot

RENT_SITE = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.90505446386719%2C%22east%22%3A-121.96160353613281%2C%22south%22%3A37.46419422792466%2C%22north%22%3A38.08508509077189%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(RENT_SITE, headers=header, timeout=60)
info = response.text

soup = BeautifulSoup(info, 'html.parser')
Links = [i.get("href") for i in soup.select("article a.jnnxAW")]
Address = [i.get_text() for i in soup.select("article a address")]
Prices = [i.get_text().strip('+ 1 bd').strip('+/mo') for i in soup.select("span.iMKTKr")]
Dict = {}
for i in range(len(Address)):
    Dict[f'{i}'] = {
        'Address': Address[i],
        'Price': Prices[i],
        'Link': Links[i]
    }

for i in range(len(Address)):
    a = Bot()
    a.Entry(add=Dict[f'{i}']['Address'], price=Dict[f'{i}']['Price'], link=Dict[f'{i}']['Link'])





