import requests # See http://docs.python-requests.org/
from settings import Settings
from external.clean_response import CleanResponse

class FetchRaces():

    def __init__(self, track, date):
        api = Settings()
        self._url = ("{}/{}/?date={}".format(api.HorseApiUrl(), track, date))

    def __repr__(self):
        return self._url

    def response(self):
        return CleanResponse(requests.get(self._url)).clean()
