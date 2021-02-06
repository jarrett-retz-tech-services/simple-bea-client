import requests
from .tables.tables import NIPA, GDPByIndustry, Regional

class Bea:
    # TODO: Only define baseUrl in one place
    # Currently it's defined here and in the base class
    baseUrl = "https://apps.bea.gov/api/data?UserID="

    def __init__(self, api_key):
        self.API_KEY = api_key
        self.NIPA = NIPA(api_key)
        self.GDPByIndustry = GDPByIndustry(api_key)
        self.Regional = Regional(api_key)

    def getDatasetList(self):

        r = requests.get(f'{self.baseUrl}{self.API_KEY}&method=GETDATASETLIST')

        try:
            r.raise_for_status() # Check for error
        except requests.exceptions.HTTPError as e:
            return e

        return r.json() # Return as JSON if no error

