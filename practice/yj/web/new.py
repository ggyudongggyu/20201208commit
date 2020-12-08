import requests
url1 = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text

from bs4 import BeautifulSoup
soup = BeautifulSoup(url1, 'lxml')

My_table = soup.find('table',{'class':'wikitable sortable'})
Countries = []
links = My_table.findAll('a')
for link in links and links != None:
    Countries.append(link.get('title'))
print(Countries)