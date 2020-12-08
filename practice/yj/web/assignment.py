from urllib.request import urlopen
from bs4 import BeautifulSoup
response = urlopen("https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B5%AC%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html,"html.parser")
mugic_dictionary={}
cnt = 1
for x in bs.find('tbody').findAll('tr'):
    line_values = x.findAll('td')
    if line_values:
        name = line_values[0].get_text()
        population = line_values[1].get_text().replace(',', '')
        if name and population:
            mugic_dictionary[cnt] = (name, int(population))
            cnt+=1
print(mugic_dictionary)




# import requests
# url1 = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text
# from bs4 import BeautifulSoup
# s = requests.Session()
# response = s.get(url1, timeout = 10)
# right_table = soup.find('table', {'class':'wikitable sortable'})




# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# response = urlopen("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
# b_html = response.read()
# s_html = b_html.decode()
# bs = BeautifulSoup(s_html,"html.parser")
# population = {}
# table = bs.find("table", class_ = "wikitable sortable")
# tables = table.find_all("tr")
# table_row = table.find_all("td")

# for table in table_row:
#     table_roww = table.find("td")
#     # table_link = table.find("a")
#     if table_roww != None :
#         table_name = table_roww.text
#         print(table_name)

# for x in bs.find('tbody').findAll('tr'):
#     ranking = x.find('td')
#     # name = x.findAll('td').find('a')
#     # nums = x.find('td', attrs={'align': 'right'})
#     # if name != None and ranking != None and nums != None:
#     #     population[ranking.text] = (name.text, nums.text)
# print(ranking)