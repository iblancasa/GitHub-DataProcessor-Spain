#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module to process languages by province
    :author: Israel Blancas Álvarez
"""


# Filename: languagesprovince.py
import json
import time

class LanguagesProvince:
    """Manage the total languages in each city"""

    cities = []
    output_file = "languagesProvince.json"


    def __init__(self, data_directory):
        """Constructor.
           :param data_directory: directory where the data is stored
           :type data_directory: str"""
        self.output_file = data_directory + "/" + self.output_file



    def addCityData(self,city,languages):
        """Add a new registry of contributions in a city
           :param city: city where store data
           :type city: str
           :param date: when was calculated the number of contributions
           :type date: str format %d/%m/%Y
        """
        self.cities.append([city,languages])




    def toFile(self):
        """Write the data in the correct JSON"""
        json_data = json.dumps(self.cities,indent=4)
        with open(self.output_file, "w") as text_file:
            text_file.write(json_data)



# End of languagesprovince.py
