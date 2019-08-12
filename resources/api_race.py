from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
import json
from models.race import Race
from external.fetch_races import FetchRaces

class ApiRace(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('track')
    parser.add_argument('day')

    @classmethod
    def get(self, id=None):
        data = ApiRace.parser.parse_args()
        races = Race(data['track'], data['day'])
        if not races.getRaces():
            external = FetchRaces(data['track'], data['day']).response()
            races.setRaces(external)
        return races.getRaces()['runs']