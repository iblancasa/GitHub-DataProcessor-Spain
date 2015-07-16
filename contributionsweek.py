#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Filename: contributionsweek.py
import json

class ContributionsWeek:
    """Manage contributions between each update, more o less one week"""

    countryContributions = 0
    totalContributions = None
    output_file = "contributionsWeek.json"
    cities = {}


    def __init__(self, data_directory,totalC):
        """Constructor.
           :param data_directory: directory where the data is stored"""

        self.totalContributions = totalC
        self.output_file = data_directory + "/" + self.output_file


    def calcule(self):
        cities = self.totalContributions.getCities()
        for city in cities:
            contributions = self.totalContributions.getCityContributions(city)
            dates = sorted(contributions, key=lambda key: contributions[key])
            last_contrib = 0
            for date in dates:
                self.addCityData(city,date,contributions[date] - last_contrib)
                last_contrib = contributions[date]
            self.addCityData(city,dates[0],0)


    def addCityData(self,city,date,contributions):
        """Add a new registry of contributions in a city
           :param city: city where store data
           :param date: when was calculated the number of contributions
           :param contributions: number total of contributions
        """
        if not city in self.cities:
            self.cities[city] = {date: contributions};
        else:
            self.cities[city][date] = contributions;


    def toFile(self):
        """Write the data in the correct JSON"""
        json_data = json.dumps(self.cities,sort_keys=True, indent=4)
        with open(self.output_file, "w") as text_file:
            text_file.write(json_data)



# End of contributionsweek.py
