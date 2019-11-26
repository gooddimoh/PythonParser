import re
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup

url = 'https://youcontrol.com.ua/catalog/kved/01/'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)

if __name__ == '__main__':
    attrs = {'href': re.compile(r'\.mid$')}

    tracks = soup.find_all('a')
    s = 0
    count = 0
    for track in tracks:
        print(track)
        count += 1

        [int(s) for s in track.split() if s.isdigit()]

        print(s)
