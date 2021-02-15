# Simple BEA Client

------------

## Installation

`pip install beasy==0.0.1a2`

## Description

This library is an unofficial Python API client for [U.S Bureau of Economic Analysis](https://www.bea.gov/ "U.S Bureau of Economic Analysis") API.

You can view the developer guide for the API [here](https://apps.bea.gov/api/_pdf/bea_web_service_api_user_guide.pdf "here"). This is **not** the user guide for this client library. However, it will provide useful information on how this library interacts with the API.

## Purpose

Other BEA client libraries exist for accessing the API. However, in my opinion, they are either too complicated or poorly conceived. Therefore, this library is a simple and straightforward client.

If complicated sorting, filtering, or formatting functions are desired, they will be added as utility functions that are not part of the client module.

## Usage

````
from beasy.beasy import Bea
API_KEY = 'C0F1CA34-149D-4D2F-90F1-11279F375B74'
client = Bea(API_KEY)
````

**Get Dataset List**

`client.getDatasetList()`

