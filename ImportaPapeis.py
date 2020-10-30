import urllib
import urllib.request
from bs4 import BeautifulSoup as BFS
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BFS(thepage, "html.parser")
    return soupdata

playerdatasaved = ""
soup = make_soup("http://fundamentus.com.br/detalhes.php")
for record in soup.findAll('tr'):
    playerdata = ""
    for data in record.findAll("a"):
        playerdata = playerdata +","+ data.text
    if len(playerdata)!=0:
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]
print(playerdatasaved)

"""header="Papel"
file = open(os.path.expanduser("papeis.csv"),"wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))"""






