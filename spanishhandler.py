#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename: spanishhandler.py
import json
import requests

class SpanishHandler:
    languagesFile = "spanishLanguages.json"
    data = None


    languages = None

    def __init__(self, data_directory):
        self.languagesFile = "./"+data_directory + "/" + self.languagesFile

        r = requests.get("https://raw.githubusercontent.com/JJ/top-github-users-data/master/data/user-data-Espa%C3%B1a.json")
        data = r.text
        self.data = json.loads(data)

    def calculeLanguages(self):
        languages = {}
        developers_with_lang = 0

        for user in self.data:
            lang = user['language']
            if lang !='':
                if not lang in languages:
                    languages[lang] = 0
                languages[lang] += 1
                developers_with_lang += 1

        self.languages = sorted(languages.items(), key=lambda x:x[1],reverse=True)

    def toFile(self):
        json_data = json.dumps(self.languages,indent=4)
        print json_data
        print self.languagesFile
        with open(self.languagesFile, "w") as text_file:
            text_file.write(json_data)



# End of languagesprovince.py
