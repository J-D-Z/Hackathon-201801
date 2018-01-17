# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:11:47 2018

@author: NHNBYB
"""

import pandas as pd
import requests


data = pd.read_csv("./dataRP.txt",sep='\t' , error_bad_lines=False )
print(data)
list(data)

#%%%%%%%%%%%%%%%%%
##API SIRENE



url = "https://prototype.api-sirene.insee.fr/ws"

def build_siret_query (rs):
    siret_query = "/siret/?q=Denomination:{}"
    return url + siret_query.format(rs)

def build_siren_query (rs):
    siren_query = "/siren?q=periode(Denomination:{})"
    return url + siren_query.format(rs)

def search_siret_rs(rs):
    return requests.get(build_siret_query(rs))

def search_siren_rs(rs):
    return requests.get(build_siren_query(rs))

cinquieme = data.iloc[5]
rs_du_cinquieme = cinquieme['RS_X']
print(rs_du_cinquieme)

requete = search_siret_rs(rs_du_cinquieme)
requete.raise_for_status()

response_data=requete.json()
print(response_data)