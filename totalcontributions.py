#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filename: totalcontributions.py
import json

class TotalContributions:
    """Manage the total contributions in each city"""

    cities = {}
    output_file = "totalContributions.json"

    def __init__(self, data_directory, cities_def):
        """Constructor.
           :param data_directory: directory where the data is stored"""

        self.output_file = data_directory + "/" + self.output_file

        try:
            with open(self.output_file) as data_file:
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



    def toFile(self):
        """Write the data in the correct JSON"""
        json_data = json.dumps(self.cities,sort_keys=True, indent=4)
        with open(self.output_file, "w") as text_file:
            text_file.write(json_data)

# End of totalcontributions.py
