from urllib.request import urlopen
from bs4 import BeautifulSoup
response = urlopen("https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1d")
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html,"html.parser")
music_dictionary = {}

for x in bs.find('tbody').findAll('tr'):
    ranking = x.find(attrs = {'class': 'ranking'})
    name = x.find(attrs = {'class' : 'name'}).find(attrs = {'class' : 'ellipsis'})
    if name != None and ranking != None:
        music_dictionary[ranking.text] = name.text
print(music_dictionary)