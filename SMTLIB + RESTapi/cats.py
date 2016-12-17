#!/usr/bin/env python


import requests
import unittest


class Catsfact():



    def TestGetCat(self):
        self.url = 'http://catfacts-api.appspot.com/api/facts'
        r = requests.get(self.url)
        facts = r.json()
        cat = facts['facts']
        catsF = str(cat)[3:-2:]
        return catsF
