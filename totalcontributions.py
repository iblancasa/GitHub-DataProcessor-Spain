#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filename: totalcontributions.py
import json
import time

class TotalContributions:
    """Manage the total contributions in each city"""

    cities = {}
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



    def getDateContributions(self,date):
        '''Helper to sort'''
        for key in date:
            return time.strptime(key, "%d-%m-%Y")



    def addCityData(self,city,date,contributions):
        """Add a new registry of contributions in a city
           :param city: city where store data
           :type city: str
           :param date: when was calculated the number of contributions
           :type date: str format %d/%m/%Y
           :param contributions: number total of contributions
           :type contributions: int
        """
        if city in self.cities:
            for d in self.cities[city]['dates']:
                for key in d:
                    if date == key:
                        self.cities[city]['dates'].remove(d)
                        self.cities[city]['dates'].append({date:contributions})
                        self.cities[city]['dates'] = sorted(self.cities[city]['dates'], key=self.getDateContributions,reverse=True)
                        return
        else:
            self.cities[city]={"dates":[]}

        self.cities[city]['dates'].append({date:contributions})
        self.cities[city]['dates'] = sorted(self.cities[city]['dates'], key=self.getDateContributions)



    def getCityContributions(self, city):
        """Return the data of one city
        :param city: city to query
        :type city: str
        :return: date - contributions dictionary
        :rtype: dict
        """
        return self.cities[city]



    def getCities(self):
        """Return all cities
        :return: all registered cities
        :rtype: dict
        """
        return self.cities.keys()



    def toFile(self):
        """Write the data in the correct JSON"""
        json_data = json.dumps(self.cities,indent=4)
        with open(self.output_file, "w") as text_file:
            text_file.write(json_data)



# End of totalcontributions.py
