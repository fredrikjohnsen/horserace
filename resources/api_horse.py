from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
import json
from models.horse import Horse
from external.fetch_races import FetchRaces

class ApiHorse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')

    @classmethod
    def get(self, id=None):
        data = ApiHorse.parser.parse_args()
        races = Horse(data['name'])
        if not races.getRaces():
            return 'No runs for that horse'
        return races.getRaces()