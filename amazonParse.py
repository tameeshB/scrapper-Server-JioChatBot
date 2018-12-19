#!/usr/bin/python

import requests, re, json, argparse, sys, os
from bs4 import BeautifulSoup
from urllib import parse

def getEl(context, tag, className):
    elemSearch = context.find_all(tag, class_=className)
    if len(elemSearch) > 0:
        return elemSearch
def getJson(keyword):
    url = "https://www.amazon.in/s/ref=nb_sb_ss_i_2_11?url=search-alias%3Daps&" + parse.urlencode({"field-keywords" : keyword})
    # print(url)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    sResult = soup.find_all('div', class_='s-item-container')

    returnList = []

    for resultItem in sResult:
        thisElem = {}
        titleSearch = resultItem.find_all('h2', class_='s-access-title')
        priceSearch = resultItem.find_all('span', class_='s-price')
        urlSearch = resultItem.find_all('a', class_='a-link-normal')
        imgSearch = resultItem.find_all('img', class_='s-access-image')
        ratingSearch = resultItem.find_all('span', class_='a-icon-alt')
        
        if len(titleSearch) > 0:
            thisElem["name"] = titleSearch[0].get_text()
        if len(priceSearch) > 0:
            priceIter = priceSearch[0].children
            try:
                next(priceIter)
                thisElem["price"] = next(priceIter)
            except StopIteration:
                thisElem["price"] = '-1'
        if len(urlSearch) > 0:
            thisElem["url"] = urlSearch[0].get('href')
        if len(imgSearch) > 0:
            thisElem["img"] = imgSearch[0].get('src')
            thisElem["rating"] = "-1"
        if len(ratingSearch) > 0:
            for ratingSearchRes in ratingSearch:
                ratingText = ratingSearchRes.get_text()
                # if "out of" in ratingText and "stars" in ratingText:
                #     thisElem["rating"] = ratingSearch[0].get_text()
                regexMatch = re.match(r"(\d+[.,]?\d*) out of 5 stars", "4.4 out of 5 stars")
                if regexMatch:
                    thisElem["rating"] = regexMatch.group(1)
                    break
        if "name" not in thisElem or "price" not in thisElem:
            continue
        returnList.append(thisElem)

    return json.dumps(returnList)

# main

# parser = argparse.ArgumentParser(description='Search amazon.in for products.')
# if len(sys.argv) == 0:
#     print(json.dumps("No search parameter found"))
#     exit(1)

def amazon_query(key):
    JSONresponse = []
    for _ in range(5):
        JSONresponse = getJson(key)
        if JSONresponse != "[]":
            break

    return JSONresponse
        
# print(json.dumps("Error or No record found"))
# exit(1)
