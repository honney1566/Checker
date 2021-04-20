import pandas as pd
from bs4 import  BeautifulSoup
import numpy as np
import requests
import time
letter_nouns=[]
def wordslist(URL):
    #Prepare data
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Take all containers
    for container in soup.find_all('div', {"class" : 'container'}):
        # If container has a price then extract:
        #Take name and price from this container
        price = soup.find_all("span", {'class': 'score'})
        for div in price:
            letter_nouns.append(div.text)
##wordslist('https://www.unscramblerer.com/4-letter-nouns/')
#wordslist('https://www.unscramblerer.com/5-letter-nouns/')
#print(letter_nouns)
letter_nouns=['cryptocurrency','dasviohfn']
#URL='https://www.namecheap.com/domains/registration/results/?domain=cryptocurrency'
#time.sleep(10)
#page = requests.get(URL)
#time.sleep(10)
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
for name in letter_nouns:
    URL='https://www.namecheap.com/domains/registration/results/?domain='+name
    time.sleep(10)
    page = requests.get(URL)
    time.sleep(10)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    if soup.find('div',{'class': 'price'}) is not None:
        print(soup.find('div',{'class': 'price'}))
        print(URL+ '  Not available')
    else:
        print(URL+ '   Available')
        print(soup.find('div', {'class': 'price'}))
