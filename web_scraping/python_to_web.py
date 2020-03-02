import requests
from bs4 import BeautifulSoup
from csv import writer
import os

url=input("Put your URL here...")
responce = requests.get(url)
soup=BeautifulSoup(responce.text,"html.parser")

'''tag = soup.b
tag.name = "hackerrank"
type(tag)
comment = soup.b.string
type(comment)
print(comment)'''
#print(tag.get('class'))
#print(soup.prettify())
#print(soup.get_text())
#print(soup.find_all())

user_input=input("enter what you want to find: ")
if 'head' in user_input:
    headers=soup.find("head").get_text().replace('\n', '')
    print(headers)
elif 'body' in user_input:
    body = soup.find("body").get_text().replace('\n', '')
    print(body)
elif 'title' in user_input:
    titles=soup.find("title").get_text().replace('\n','')
    soup.title # <title>The Dormouse's story</title>
    soup.title.name
    soup.title.string # u'The Dormouse's story'
    soup.title.parent.name # u'head'
    print(titles)
    
elif 'paragraph' or 'p' in user_input:
    #soup.p['class'] # u'title'
    para=soup.find("p").get_text().replace('\n','')
    print(para)
elif 'heading' or 'b' in user_input:
    haeding = soup.body.b.get_text().replace('\n', '')
    print(haeding)
elif 'lists' in user_input:
    for lists in soup.find_all('li'):
        print(lists.get('li'))

elif 'ul' or "uper list" in user_input:
    for ul in soup.find_all('ul'):
        print(ul.get('ul'))

elif 'link' or 'a' in user_input:
    for link in soup.find_all('a'):
        print(link.get('href'))
