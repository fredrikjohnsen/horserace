class Settings():

    def __init__(self):
        self.horse_api_url = 'http://www.travsport.no/Sport/Resultater'
        self.mongo_uri = 'mongodb://localhost:27017/horserace'
        self.mongo_db = 'horserace'

    def HorseApiUrl(self):
        return self.horse_api_url

    def MongoURI(self):
        return self.mongo_uri

    def MongoDb(self):
        return self.mongo_db