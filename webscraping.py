
#import the library used to query a website
import urllib2 #if you are using python3+ version, import urllib.request

#specify the url
wiki = "https://en.wikipedia.org/wiki/GNOME_Shell"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki) #For python 3 use urllib.request.urlopen(wiki)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

#html function of beautifulsoup use for scraping 
print soup.prettify()

#Work with HTML tags

soup.title

soup.title.string

soup.a 
# use for any containt like html tag 
soup.find_all("")

# find table of any website
all_tables=soup.find_all('table')

#right table need 
soup.find_all('table',class_='wikitable sortable')

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df

