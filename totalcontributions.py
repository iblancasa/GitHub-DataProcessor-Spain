#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filename: TotalContributions.py
import json

class TotalContributions:
    """Manage the total contributions in each city"""

    countryContributions = 0
    cities = {}

    def __init__(self, data_directory, cities_def):
        """Constructor.
           :param data_directory: directory where the data is stored"""

        try:
            with open(data_directory+'totalContributions.json') as data_file:
                cities = json.load(data_file)
        except IOError:
            print ("\033[93m No total contributions file was detected \033[0m")

    def addCityData(self,city,date,contributions):
        """Add a new registry of contributions in a city
           :param city: city where store data
           :param date: when was calculated the number of contributions
           :param contributions: number total of contributions
        """
        self.cities[city] = {date: contributions};
        self.countryContributions += contributions
        print(self.cities)

# End of TotalContributions.py
