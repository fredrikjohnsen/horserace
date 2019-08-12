from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from db import mongo
from settings import Settings

from flask_restful import Resource, Api

app = Flask(__name__)
CORS(app)
settings = Settings()
app.config['MONGO_DBNAME'] = settings.MongoDb()
app.config['MONGO_URI'] = settings.MongoURI()
mongo.init_app(app)
from resources.api_race import ApiRace
api = Api(app)

api.add_resource(ApiRace, '/race/<string:id>')

@app.route("/")
def home_page():
    return '<h1>Horserace</h1>'

if __name__ == '__main__':
    app.run(debug=True)