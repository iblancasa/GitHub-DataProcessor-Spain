#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from totalcontributions import *
import time

data_directory = "ProcessedData"


with open('cities.json') as data_file:
    cities = json.load(data_file)


totalContributions = TotalContributions(data_directory,cities);


'''
for city in cities:
    url = 'https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-'+city['city'].encode('utf-8')+'.json'
    r = requests.get(url)
    data = r.text
'''

name = 'Granada'
url = 'https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-'+name+'.json'
r = requests.get(url)
data = r.text
data = json.loads(data)

#Contribuciones totales
contributions = 0;
languages = {};

for user in data:
    contributions+=user['contributions']

#totalContributions.addCityData(name,time.strftime("%d/%m/%Y"),contributions)

#totalContributions.toFile();
