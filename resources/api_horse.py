from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
from models.horse import Horse

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