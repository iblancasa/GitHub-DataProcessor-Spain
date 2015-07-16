#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from totalcontributions import *
from contributionsweek import *
import time

data_directory = "ProcessedData"


with open('cities.json') as data_file:
    cities = json.load(data_file)


totalContributions = TotalContributions(data_directory);


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

contributions = 0;
languages = {};

for user in data:
    contributions+=user['contributions']
    lang = user['language'].encode('utf-8')

    if not lang in languages:
        languages[lang] = 0
    languages[lang] +=1

totalContributions.addCityData(name,time.strftime("%d/%m/%Y"),contributions) #Add total contributions



contributionsWeek = ContributionsWeek(data_directory,totalContributions) #Create contributions week object
contributionsWeek.calcule() #Calcula contributions week
