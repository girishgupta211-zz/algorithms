import requests
from bs4 import BeautifulSoup

url = 'https://www.espncricinfo.com/series/8039/commentary/1144520/england-vs-india-38th-match-icc-cricket-world-cup-2019'
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
deliveries = []

for item in soup.find_all('div', {"class": "commentary-item"}):
    deliver_no_span = item.find('div',
                                {"class": "time-stamp"})
    delivery_outcome = item.find('span',
                                 {"class": "over-score"})
    delivery_no = ''
    outcome = ''
    if deliver_no_span and delivery_outcome:
        delivery_no = deliver_no_span.text.strip().encode('ascii',
                                                          'ignore').decode(
            "utf-8")

        outcome = delivery_outcome.text.strip().encode(
            'ascii', 'ignore').decode("utf-8")

        deliveries.append(
            {"delivery_no": str(delivery_no), "outcome": outcome})

print(deliveries)
