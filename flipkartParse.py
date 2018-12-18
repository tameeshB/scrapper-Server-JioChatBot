import sys
import urllib
import json
from bs4 import BeautifulSoup

if(len(sys.argv)>1):
	url = sys.argv[1]
else
	url = "https://www.flipkart.com/search?q=mobiles"
	
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

obje = []
err = 0

for obje in soup.find_all('a', class_="_31qSD5"): 
	dic = {}
	for link in obje.find_all('img', class_="_1Nyybr"):
		dic["name"] = link.get('alt')
		dic["url"] = link.get('src')
	if(len(dic)!=2):
		continue

	for link in obje.find_all('div', class_="_1vC4OE"):
		dic["price"] = link.get_text()
	if(len(dic)!=3):
		continue

	for link in obje.find_all('div', class_="hGSR34"):
		dic["rating"] = link.get_text()
	if(len(dic)!=4):
		continue

	obje.append(dic)


out = json.dumps(obje)

print(out)
