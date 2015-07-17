#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filename: totalcontributionspopulation.py
import json
import time

class TotalContributionsPopulation:
    """Manage the total contributions / population in each city"""

    cities = []
    output_file = "totalContributionsPopulation.json"
    totalContributions = None


    def __init__(self, data_directory, totalC):
        """Constructor.
           :param data_directory: directory where the data is stored
           :type data_directory: str
           :param totalC: total contributions in all cities
           :type TotalContributions"""
        self.output_file = data_directory + "/" + self.output_file
        self.totalContributions = totalC


    def getCity(self,name):
        """Get data from a city
           :param name: name of a city
           :type name: str"""
        for city in self.cities:
            if city[0] == name:
                return city
        return None


    def getDateContributions(self,date):
        """Helper to sort
           :param date: date/contributions dictionary
        """
        for key in date:
            return time.strptime(key, "%d-%m-%Y")


    def getLastContibutions(self,city):
        """Get last number of contributions from the list
        :param city: city to get last number of contributions
        :type city: str"""
        for d in city[1][0]:
            return city[1][0][d]

    def getContrib(self, contrib):
        """Get number of contributions
           :param contrib: dictionary --> date, contributions"""
        for k in contrib:
            return contrib[k]

    def getDate(self, date):
        """Get date of contributions
           :param date: dictionary --> date, contributions"""
        for k in date:
            return k

    def getPopulation(self, cities,name):
        """Get population from a city
           :param cities
        """
        for city in cities:
            if city["city"]==name:
                return city['population']


    def calcule(self, population):
        """Calcule el number de contributions/population in each city
           :param population: dictionary --> city: name_city, population: number
        """
        for city in self.totalContributions.cities:
            name = city[0]
            contributions = city[1]

            for contrib in contributions:
                habitants = self.getPopulation(population,name)
                contrib_data = float(self.getContrib(contrib)) / float(habitants)
                contrib_data = round(contrib_data,4)
                self.addCityData(name,self.getDate(contrib),contrib_data)


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

# End of totalcontributions.py
