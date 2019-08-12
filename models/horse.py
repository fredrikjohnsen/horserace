from db import mongo
from bson.json_util import dumps
import json
class Horse():
    db = mongo.db.races
    def __init__(self, name):
        self.name = name
        self.runs = []

    def getRaces(self):
        pipeline = [
           {"$match" : {"runs.name" : self.name}},
            {"$unwind": "$runs"},
            {"$match" : {"runs.name" : self.name}},
            ]
        race = self.db.aggregate(pipeline)
        print(race)
        current = []
        for run in race:
            print(run)
            current.append({"horse": dumps(run)})
        return current