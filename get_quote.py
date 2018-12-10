from bs4 import BeautifulSoup
import requests
from datetime import datetime

def get_quote():
    #Using eduro.com for getting quote
    url = 'https://www.eduro.com/'

    date = datetime.now().strftime('%d')
    time = datetime.now().strftime('%H:%M:%S')
    timefor = "17:00:00"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    quote_date = soup.find("div", {"class":"dates"}).text
    quote = soup.find("dailyquote").text

    if quote_date == date:
        message = "Quote Of The Day: \n\n" + quote.strip()
        return message
