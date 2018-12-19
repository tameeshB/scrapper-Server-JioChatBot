import sys
import urllib
import json
from bs4 import BeautifulSoup


def flipkart_query(key, minp, maxp):

	Min = -1
	Max = -1

	if(key!=""):
		query = key
		keyword = {}
		keyword["q"] = query
		Min = minp
		Max = maxp

		if(Min==-1 or Min=="-1"):
			price_range = "&p%5B%5D=facets.price_range.from%3DMin"
		else:
			price_range = "&p%5B%5D=facets.price_range.from%3D" + str(Min)
			
		if(Max==-1 or Min=="-1"):
			price_range = "&p%5B%5D=facets.price_range.to%3DMax"
		else:
			price_range = "&p%5B%5D=facets.price_range.to%3D" + str(Max)
		 
		url = "https://www.flipkart.com/search?" + urllib.parse.urlencode(keyword) + price_range
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
			dic["price"] = link.get_text()[1:]
		if(len(dic)!=3):
			continue

		for link in obje.find_all('div', class_="hGSR34"):
			dic["rating"] = link.get_text()
		if(len(dic)!=4):
			continue

		obj.append(dic)


	out = json.dumps(obj)

	return out
