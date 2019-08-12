from db import mongo
from bson.json_util import dumps
import json
class Horse():
    db = mongo.db.races
    def __init__(self, name):
        self.name = name
        self.runs = []

    def getRaces(self):
        race = self.db.find({"runs.name" : self.name})
        current = []
        for run in race:
            current.append({'track' : run['track'], 'date' : run['date']})
        return current