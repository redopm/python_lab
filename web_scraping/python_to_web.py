import requests
from bs4 import BeautifulSoup
from csv import writer


url=input()
responce = requests.get(url)
soup=BeautifulSoup(responce.text,"html.parser")
headers=soup.find("head").get_text().replace('\n', '')
#print(headers)
body = soup.find("body").get_text().replace('\n', '')
print(body)

