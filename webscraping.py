import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

datasaved = ""
soup = make_soup("http://fundamentus.com.br/detalhes.php")
tables = soup.find_all('tbody')
cnt = 0
for my_table in tables:
    cnt += 1
#    print ('=============== TABLE {} ==============='.format(cnt))
    rows = my_table.find_all('tr', recursive=False)                  # <-- HERE
    for row in rows:
        cells = row.find_all(['th', 'td'], recursive=False)          # <-- HERE
        loop = ""
        for cell in cells:
            # DO SOMETHING
            loop = loop + cell.text +","
        datasaved = datasaved +"\n"+ loop[1:]

        header="Papel, Nome Comercial, Razão Social"+"\n"
        file = open(os.path.expanduser("papeis.csv"), "wb")
        file.write(bytes(header, encoding="ascii", errors='ignore'))
        file.write(bytes(loop, encoding="ascii", errors='ignore'))

