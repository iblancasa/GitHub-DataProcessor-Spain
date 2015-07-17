#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filename: totalcontributions.py
import json
import time

class TotalContributions:
    """Manage the total contributions in each city"""

    cities = []
    output_file = "totalContributions.json"


    def __init__(self, data_directory):
        """Constructor.
           :param data_directory: directory where the data is stored
           :type data_directory: str"""
        self.output_file = data_directory + "/" + self.output_file

        try:
            with open(self.output_file) as data_file:
                self.cities = json.load(data_file)
        except IOError:
            print ("\033[93m No total contributions file was detected \033[0m")

    def getCity(self,name):
        """Get data from a city.
           :param name: name of a city
           :type name: str """
        for city in self.cities:
            if city[0].encode('utf-8') == name:
                return city
        return None


    def getDateContributions(self,date):
        """Helper to sort
        :param date: one date,contribution
        """
        for key in date:
            return time.strptime(key, "%d-%m-%Y")


    def getLastContibutions(self,city):
        """Get last number of contributions from the list
        :param city: city to get last number of contributions
        :type city: str""" 
        for d in city[1][0]:
            return city[1][0][d]


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
