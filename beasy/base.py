import requests

class Base:
    baseUrl = "https://apps.bea.gov/api/data?"

    def __init__(self, datasetName, apiKey):
        self.datasetName = datasetName
        self.apiKey = apiKey

    def getParameterList(self):
        method = "GetParameterList"

        parameters = {
            'UserID': self.apiKey,
            'method': method,
            'datasetname': self.datasetName,
        }

        r = requests.get(self.baseUrl, params=parameters)
        
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        
        return r.json()

    def getParameterValues(self, parameter):
        method = "GetParameterValues"

        parameters = {
            'UserID': self.apiKey,
            'method': method,
            'datasetname': self.datasetName,
            'parametername': parameter
        }

        r = requests.get(self.baseUrl, params=parameters)
        
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        
        return r.json()

    def getParameterValuesFiltered(self, targetParameter, **kwargs):
        method = 'GetParameterValuesFiltered'

        parameters = {
            'UserID': self.apiKey,
            'method': method,
            'datasetname': self.datasetName,
            'targetparameter': targetParameter,
            **kwargs
        }
        r = requests.get(self.baseUrl, params=parameters)
        
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        
        return r.json()

    def getData(self, **kwargs):
        method = "GetData"
        
        parameters = {
            'UserID': self.apiKey,
            'method': method,
            'datasetname': self.datasetName,
            **kwargs
        }

        r = requests.get(self.baseUrl, params=parameters)
        
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        
        return r.json()
