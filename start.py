#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Module to process data from https://github.com/JJ/top-github-users-data
    :author: Israel Blancas Álvarez
"""

import json
import requests
from totalcontributions import *
from contributionsweek import *
from totalcontributionspopulation import *
from languagesprovince import *
import time

data_directory = "ProcessedData"


with open('cities.json') as data_file:
    cities = json.load(data_file,'utf-8')
print '\033[95m'+"Cities data loaded"+'\033[0m'



totalContributions = TotalContributions(data_directory);
languagesProvince = LanguagesProvince(data_directory)


print '\033[95m'+"Downloading data"+'\033[0m'

for city in cities:
    name = city['city'].encode('utf-8')
    url = 'https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-'+name+'.json'
    r = requests.get(url)
    data = r.text
    data = json.loads(data)
    print '\033[94mData from '+name+' received\033[0m'
    contributions = 0;
    languages = {};

    for user in data:
        contributions+=user['contributions']
        lang = user['language']

        if not lang in languages:
            languages[lang] = 0
        languages[lang] +=1


    totalContributions.addCityData(city['city'],time.strftime("%d-%m-%Y"),contributions) #Add total contributions
    print '\033[94m \t\t Total contributions from '+name+' calculated\033[0m'
    languagesProvince.addCityData(city['city'],languages)
    print '\033[94m \t\t Total languages from '+name+' calculated\033[0m'



contributionsWeek = ContributionsWeek(data_directory,totalContributions) #Create contributions week object
contributionsWeek.calcule() #Calcule contributions week
print '\033[94m Contributions / week calculated\033[0m'


totalContributionsPopulation = TotalContributionsPopulation(data_directory,totalContributions)
totalContributionsPopulation.calcule(cities)
print '\033[94m Contributions / population calculated\033[0m'


totalContributionsPopulation.toFile()
contributionsWeek.toFile()
totalContributions.toFile()
languagesProvince.toFile()
print '\033[94m Saving all data to files\033[0m'
