from db import mongo
import json
class Race():
    db = mongo.db.races
    def __init__(self, track, date):
        self.track = track
        self.date = date
        self.runs = []

    def getRaces(self):
        race = self.db.find_one({"track" : self.track, 'date' : self.date})
        if race:
            return race
        else:
            return None

    def setRaces(self, runs):
        test = self.db.insert({"track": self.track, "date" : self.date, "runs" : runs})
        print(test)
        return runs