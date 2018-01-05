import requests
from bs4 import BeautifulSoup

url = "http://stateoftheunion.onetwothree.net/texts/"
response = requests.get(url)

page = BeautifulSoup(response.content, "html5lib")
table = page.findAll('li')
for x in table:
    if x:
        link = x.find('a').get('href')
        url2 = url + link
        name = link.split(".")[0]
        if name == "":
            continue
        f = open(name + "new.txt", "w")
        f.write("***\n")
        response2 = requests.get(url2)
        page2 = BeautifulSoup(response2.content, "html5lib")
        table2 = page2.findAll('p')
        date = page2.findAll('h3')
        print(link)
        if date:
            f.write(date[0].text)
        for t in table2:
            if t:
                f.write(t.text + "\n")
        f.close()
