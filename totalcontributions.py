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



    def addCityData(self,city,date,contributions):
        """Add a new registry of contributions in a city
           :param city: city where store data
           :type city: str
           :param date: when was calculated the number of contributions
           :type date: str format %d/%m/%Y
           :param contributions: number total of contributions
           :type contributions: int
        """
        for key in self.cities:
            name = key[0].encode('utf-8')
            if name == city:
                key[1][date]=contributions
                return


        new = [city, {date: contributions}]
        self.cities.append(new)


''''
        if city in self.cities:
            print "SE CUMPLE"
            print city
            self.cities[city][date] = contributions;

        else:
            print city
            self.cities[city] = {date: contributions};
'''
'''
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


    def changeFormat(self,date):
        return time.strptime(date[0], "%d-%m-%Y")

    def getDate(self,it):
        fechas = it[1]
        fechas = fechas.items()
        fechas = sorted(fechas, key=self.changeFormat,reverse=True)
        return fechas[0][1]

    def toFile(self):
        """Write the data in the correct JSON"""
        it = self.cities.items()
        it = sorted(it, key=self.getDate,reverse=True)

        json_data = json.dumps(it,indent=4)
        with open(self.output_file, "w") as text_file:
            text_file.write(json_data)

'''

# End of totalcontributions.py
