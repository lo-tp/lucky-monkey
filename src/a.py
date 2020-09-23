import requests
from sys import argv
from json import dumps, loads
from requests.exceptions import HTTPError

data = {
    "api_name": "stock_basic",
    "token": argv[1],
    "params": {
        "list_stauts": "L"
    },
    "fields": "ts_code,name,area,industry,list_date"
}


def sendRequest():
    try:
        response = requests.post(
            "http://api.waditu.com",
            data=dumps(data))
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        content = response.content
        print(response.json())
        print('Success!')


sendRequest()
