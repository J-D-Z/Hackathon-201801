# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:40:30 2018

@author: NHNBYB
"""

#%% Exemple sur ouisncf
def nettoyage(reponse):
    res=reponse.replace("\'","")
    res=res.replace('\\"','"')
    res=res.replace('"{','{')
    res=res.replace('}"','}')
    res=res.replace('//','')
    res=res.replace('="','')
    res=res.replace('">','')
    res=res.replace(';"','')
    return res

import os
import requests

os.chdir('D:/NHNBYB/Mes Documents/Webscraping/Scraping SNCF/')
headers = {
    'Host': 'www.oui.sncf',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json;charset=utf-8',
    'X-VSD-SMART-GUY-GUARD': 'SdulvOlooN5;44534:T4QQRZD\\',
    'X-VSD-LOCALE':'fr_FR',
    'Referer': 'https://www.oui.sncf/proposition?clientId=8cf49d04-2ced-400e-838f-18056a134b51&language=fr&country=FR',
    'Content-Length': '1129',
    'Connection': 'keep-alive'
}

url='https://www.oui.sncf/proposition/rest/search-travels/outward'

demande1='{"origin":"'+ville_depart+'","originLocation":{"id":null,"label":null,"longitude":null,"latitude":null,"type":null,"country":null,"stationCode":null,"stationLabel":null},"destination":"'+ville_arrivee+'","destinationCode":null,"destinationLocation":null,"directTravel":false,"asymmetrical":false,"professional":false,"customerAccount":false,"oneWayTravel":true,"departureDate":"'+date+'T'+horaire+'","returnDate":null,"travelClass":"SECOND","country":"FR","language":"fr","busBestPriceOperator":null,"passengers":[{"travelerId":null,"profile":"ADULT","age":26,"birthDate":null,"fidelityCardType":"NONE","fidelityCardNumber":null,"commercialCardNumber":null,"commercialCardType":"NONE","promoCode":"","lastName":null,"firstName":null,"phoneNumer":null,"hanInformation":null}],"animals":[],"bike":"NONE","withRecliningSeat":false,"physicalSpace":null,"fares":[],"withBestPrices":false,"highlightedTravel":null,"nextOrPrevious":false,"source":"FORM_SUBMIT","targetPrice":null,"han":false,"outwardScheduleType":"BY_DEPARTURE_DATE","inwardScheduleType":"BY_DEPARTURE_DATE","$initial":true,"$queryId":"WDDI9"}'


r = requests.post(url, data=demande1,headers=headers)

#La requête a-t-elle fonctionne ? On veut 200
print("Billet " + ville_depart + "-" + ville_arrivee + "   Statut : "+str(r))

#Voici notre resultat ; il faut nettoyer la chaîne de caracteres maintenant
resultat=nettoyage(r.text)
print(resultat)


#%% Sur pages-jaunes
import os
import requests
import json

os.chdir('D:/NHNBYB/Mes Documents/Webscraping/Scraping SNCF/')

headers = {
    'Host':'www.pagesjaunes.fr',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.pagesjaunes.fr/',
    'Cookie': 'nav=1; pjtmctxv1=300bc961-3316-464b-c695-3b4dc1f54ff5-9266cc-4e0f#7a2eea2a-8983-4633-864e-ced69e904bcc#W83FB#N#b74e42bd-4451-471f-916d-25a1f4c509de#W12ACC#20180117#7304097d6024466b4dc35332517217a1; datadome=AHrlqAAAAAMAuJwMlOBjMW4AuRi5ww==; VisitorID=195151620111266107; dtCookie=|X2RlZmF1bHR8MA; OAX=64262e5feb670c41; xtvrn=$483323$; xtan=-; xtant=1; rdmvalidation=1; pj_policy_cookie=1; kameleoonPersonalizationTargeted-20843=false/1516201114020; gig_hasGmid=ver2; tosend=%7B%22p%22%3A%7B%22tracker%22%3A%22pages-jaunes%22%2C%20%22url%22%3A%22https%3A//www.pagesjaunes.fr/%22%2C%20%22mtime%22%3A1516201113000%2C%20%22ref%22%3A%22https%3A//www.google.fr/%22%2C%20%22dest%22%3A%22https%3A//www.pagesjaunes.fr/recherche/villeneuve-sur-lot-47/olibrem%22%7D%2C%22d%22%3A%7B%22dv%22%3A%22NA%22%7D%2C%20%22t%22%3A%7B%22iplobserverstart%22%3A%221516201113071%22%2C%22jsinit%22%3A%221516201113556%22%2C%22domload%22%3A%221516201115490%22%2C%22submitform%22%3A%221516201135594%22%2C%22unload%22%3A%221516201136937%22%7D%7D',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

url='https://www.pagesjaunes.fr/recherche/59122-cambrai/tereos'


demande={'Content-Type: application/x-www-form-urlencoded',
   'Content-Length: 327',
   'quoiqui=intermarch%C3%A9&ou=paris+13&idOu=&acOuSollicitee=1&rangOu=&sourceOu=&typeOu=&nbPropositionOuTop=5&nbPropositionOuHisto=0&ouSaisi=paris+13&ouNbCar=&acQuiQuoiSollicitee=1&rangQuiQuoi=&sourceQuiQuoi=&typeQuiQuoi=&idQuiQuoi=&nbPropositionQuiQuoiTop=5&nbPropositionQuiQuoiHisto=0&quiQuoiSaisi=intermarch%C3%A9&quiQuoiNbCar='}


r = requests.post(url, data=demande,headers=headers)
r
r=requests.post(url)


#%%Pour copier quelque-chose dans le presse-papier

import pyperclip
pyperclip.copy(r.text)


#%%

https://www.pagesjaunes.fr/recherche/paris-13e-arrondissement-75/intermarche



#%% Tuto webscraping

import requests


# Requête GET sur l'url correspondant à la page d'accueil de l'Insee.
response = requests.get('https://insee.fr/fr/accueil')

print('Url: %s' % response.url)
print('Statut: %s' % response.status_code)
print(response.text)


# Écrivons une page html basique, qui dit "Hello World".
html = """<!DOCTYPE html>
<html>
    <head>
        <title>Hello World</title>
        <meta author="Paul Andrey"/>
    </head>
    <body>
        <center>Hello World!</center>
    </body>
</html>
"""
with open('hello.html', mode='w', encoding='utf-8') as html_file:
    html_file.write(html)

# Par la suite, nous rendrons le HTML directement dans le notebook, comme suit :
from IPython.core.display import HTML
HTML(html)

from bs4 import BeautifulSoup

# Parsons le html de la page d'accueil de l'Insee.
soup = BeautifulSoup(response.text, 'html.parser')
















































