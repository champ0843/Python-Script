from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
wiki="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page=request.urlopen(wiki)
soup=BeautifulSoup(page,features="html.parser")
#print(page)
#print(soup.prettify())
print(soup.title.sting)
table=soup.find('table',class_='wikitable sortable plainrowheaders')
print(table.prettify())
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in table.find_all("tr"):
    cells=row.find_all("td")
    states=row.find_all("th")
    if len(cells)==6:
        A.append(cells[0].find(text=True).strip())
        B.append(states[0].find(text=True).strip())
        C.append(cells[1].find(text=True).strip())
        D.append(cells[2].find(text=True).strip())
        E.append(cells[3].find(text=True).strip())
        F.append(cells[4].find(text=True).strip())
        G.append(cells[5].find(text=True).strip())





df=pd.DataFrame(A,columns=['Number'])
df['States']=B
df['Admin Capital']=C
df['Legislative Capital']=D
df['Judiciary Capital']=E
df['Year Capital']=F
df['Former Capital']=G
df.to_csv("UNION TERRITORY AND ELSE.csv")
print(type(soup))
