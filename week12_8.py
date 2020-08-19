import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl


url1=input("Enter url - ")
uh=urllib.request.urlopen(url1)
html=uh.read()
soup=BeautifulSoup(html,'html.parser')

sum=0
tags = soup('span')
for tag in tags:
    sum+=float(tag.contents[0])

print(sum)