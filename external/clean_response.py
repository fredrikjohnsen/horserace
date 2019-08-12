import sys, os
import dateutil.parser as dp
from bs4 import BeautifulSoup
import re

class CleanResponse():

    def __init__(self, response):
        self.response = response

    def clean(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        innerPages = soup.findAll('tbody')
        placeholder = innerPages
        ok = []
        header = None
        for helper in placeholder:
            for things in helper.findAll('tr'): 
                if len(things.findAll('td')) == 3:
                    header = self.makeHeader(things.findAll('td'))
                if len(things.findAll('td')) == 9:
                    ok.append(self.makeMyHorse(things.findAll('td'), header))

        return ok

    def toDate(self, entry):
        test = re.findall("[0-9]{2}", entry)
        return '{}.{}.{} {}:{}'.format(test[0],test[1], test[2]+test[3], test[4], test[5])
    
    def raceName(self, race):
        return race [10:-1]

    def makeMyHorse(self, h, header):
        horse = {"place" : h[0].text,
                "start" : h[1].text,
                "name" : h[2].text,
                "dist" : h[3].text,
                "time" : h[4].text,
                "kmt" : h[5].text,
                "price" : h[6].text,
                "skip" : h[7].text,
                "odds" : h[8].text
                }
        horse['meta']= header
        return horse

    def makeHeader(self, h):
        header = {
            "runtime" :   self.toDate(h[0].text),
            "racename" :   self.raceName(h[2].text),
        }
        return header