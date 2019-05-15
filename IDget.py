import requests
from bs4 import BeautifulSoup

base = 'https://offcampus.uwo.ca/Listings/Details/'
count = 0

ID_file = open('listingID.txt', 'w', encoding='utf-8')

for i in range(5000):
    url = base + str(i)
    r = requests.get(url)
    text = r.text
    print(text)
    if 'The specified URL cannot be found' in r.text:
        count = count + 1
    else:
        ID_file.write(url + ',')

ID_file.close()

print(count)
