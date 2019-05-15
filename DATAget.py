import requests
from bs4 import BeautifulSoup

file = open('listingID.txt', 'r', encoding='utf-8')

url_list = []

for line in file:
    url_list = line.split(",")

file.close()

for i in url_list:
    url = requests.get(i)
    soup = BeautifulSoup(url.text, 'html.parser')

    email = soup.find(id='ContactEmail')

    email = str(email)
    string_email = email[66:-3]
    if len(string_email) != 0:
        print(string_email)



