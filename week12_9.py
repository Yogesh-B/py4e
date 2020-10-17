
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1=input("Enter url : ")  #initial input



#finding 18th name 7times
for i in range(7):
    #url search
    html1=urllib.request.urlopen(url1,context=ctx).read()
    soup1=BeautifulSoup(html1,'html.parser')
    tags=soup1('a')
    url1=tags[1].get('href',None)
    print(tags[1].contents[0],end=' ')
