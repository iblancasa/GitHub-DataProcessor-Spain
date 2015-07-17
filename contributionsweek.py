#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Module to process contributions / week
    :author: Israel Blancas Álvarez
"""

# Filename: contributionsweek.py
import json
import time

class ContributionsWeek:
    """Manage the week contributions in each city"""

    cities = []
    output_file = "contributionsWeek.json"
    totalContributions = None


    def __init__(self, data_directory, totalC):
        """Constructor.
           :param data_directory: directory where the data is stored
           :type data_directory: str"""
        self.output_file = data_directory + "/" + self.output_file
        self.totalContributions = totalC


    def getCity(self,name):
        for city in self.cities:
            if city[0] == name:
                return city
        return None


    def getDateContributions(self,date):
        '''Helper to sort'''
        for key in date:
            return time.strptime(key, "%d-%m-%Y")


    def getLastContibutions(self,city):
        for d in city[1][0]:
            return city[1][0][d]

    def getContrib(self, contrib):
        for k in contrib:
            return contrib[k]

    def getDate(self, date):
        for k in date:
            return k

    def calcule(self):
        for city in self.totalContributions.cities:
            name = city[0]
            contributions = reversed(city[1])

            last_contrib = 0
            first = True

            for contrib in contributions:
                diff = self.getContrib(contrib) - last_contrib
                last_contrib = self.getContrib(contrib)

                if not first:
                    self.addCityData(name,self.getDate(contrib),diff)
                else:
                    self.addCityData(name,self.getDate(contrib),0)
                    first = False


    def addCityData(self,city,date,contributions):
        """Add a new registry of contributions in a city
           :param city: city where store data
           :type city: str
           :param date: when was calculated the number of contributions
           :type date: str format %d/%m/%Y
           :param contributions: number total of contributions
           :type contributions: int
        """
        city_data = self.getCity(city)

        if city_data == None:
            self.cities.append([city,[{date : contributions}]])
            self.cities = sorted(self.cities, key=self.getLastContibutions,reverse=True)
        else:
            for contrib in city_data[1]:
                for k in contrib:
                    if  k==date:
                        contrib[k]=contributions
                        city_data[1] = sorted(city_data[1], key=self.getDateContributions,reverse=True)
                        self.cities = sorted(self.cities, key=self.getLastContibutions,reverse=True)
                        return
            city_data[1].append({date : contributions})
            city_data[1] = sorted(city_data[1], key=self.getDateContributions,reverse=True)
            self.cities = sorted(self.cities, key=self.getLastContibutions,reverse=True)


    def getCityContributions(self, city):
        """Return the data of one city
        :param city: city to query
        :type city: str
        :return: date - contributions dictionary
        :rtype: dict
        """
        return self.cities[city]['dates']



    def toFile(self):
        """Write the data in the correct JSON"""
        json_data = json.dumps(self.cities,indent=4)
        with open(self.output_file, "w") as text_file:
            text_file.write(json_data)


# End of contributionsweek.py
