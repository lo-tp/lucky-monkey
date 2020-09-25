import requests
from sys import argv
from json import dumps
from requests.exceptions import HTTPError


def sendRequest(arg):
    try:
        response = requests.post(
            "http://api.waditu.com",
            data=dumps(arg))
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        return response.json()


if __name__ == "__main__":
    data = {
        "api_name": "daily",
        "token": argv[1],
        "params": {
            "ts_code": "1A0001",
            "start_date": 20181010,
            "end_date": 20181020
        },
        "fields": "ts_code, trade_date, open"
    }
    print(sendRequest(data))
