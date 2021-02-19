# Simple BEA Client

------------

## Installation

`pip install beasy==0.0.1a3`

## Description

This library is an unofficial Python API client for [U.S Bureau of Economic Analysis](https://www.bea.gov/ "U.S Bureau of Economic Analysis") API.

You can view the developer guide for the API [here](https://apps.bea.gov/api/_pdf/bea_web_service_api_user_guide.pdf "here"). This is **not** the user guide for this client library. However, it will provide useful information on how this library interacts with the API.

## Purpose

Other BEA client libraries exist for accessing the API. However, in my opinion, they are either too complicated or poorly conceived. Therefore, this library is a simple and straightforward client.

If complicated sorting, filtering, or formatting functions are desired, they will be added as utility functions that are not part of the client module.

## Usage

Currently, the library is designed to return JSON response objects from the BEA API, not XML.

````
from beasy.beasy import Bea
API_KEY = 'your_api_key'
client = Bea(API_KEY)
````

### **Get Dataset List**

"...retrieves a list of the datasets currently offered."

`client.getDatasetList()`

### **Get Parameter List**

"...retrieves a list of the parameters(required and optional) for a particular dataset."

*client.[table_name].getParameterList()*

`client.Regional.getParameterList()`

### **Get Parameter Values**

"...retrieves a list of the valid values for a particular parameter."

*client.[table_name].getParameterValues(parameter)*

`client.Regional.getParameterValues('LineCode')`

### **Get Parameter Values Filtered**

"...retrieves a list of the valid values for a particular parameter based on other provided parameters."

*client.[table_name].getParameterValuesFiltered(targetParameter, \*\*kwargs)*

`client.Regional.getParameterValuesFiltered('LineCode', 'SAINC1')`


### **Get Data**

*client.[table_name].getData(\*\*kwargs)*

`client.Regional.getData(TableName='CAINC1',
    LineCode='3',
    GeoFIPS='DE',
    Year='2014')`