import sys
import urllib
import json
from bs4 import BeautifulSoup

if(len(sys.argv)>1):
	query = sys.argv[1]
	query = "%20".join(query.split())
	url = "https://www.flipkart.com/search?q=" + query
else:
	url = "https://www.flipkart.com/search?q=mobiles"

print(url)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

obj = []
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

	obj.append(dic)


out = json.dumps(obj)

print(out)
