import json
import requests

BASE_URL = 'https://inventory-service.tixuk.io/api/v4/availability/products/1587/quantity/1/from'
INCORRECT_DATES_IN_PAST = '20220210/to/20220215'
CORRECT_DATES_IN_FUTURE = '20220319/to/20220320'
HEADER =  {"affiliateId": "londontheatredd"}

def make_request(headers, endpoint, dates, method="GET", params=''):
    _url_request = f"{endpoint}/{dates}/{params}"
    
    response = requests.request(
        method,
        _url_request,
        headers=headers,
        params=params
    )
    data = json.loads(response.text)
    return data


def scenario_one():
    hit_response = make_request(HEADER, BASE_URL, CORRECT_DATES_IN_FUTURE)
    assert hit_response.status_code == 200


def scenario_two():
    hit_response = make_request(BASE_URL, CORRECT_DATES_IN_FUTURE)
    assert hit_response.status_code == 404


def scenario_three():
    hit_response = make_request(HEADER, BASE_URL, INCORRECT_DATES_IN_PAST)
    assert hit_response.status_code == 400
    

wrong_response = {
    "request": {
        "body": "",
        "query": {
            "param": "5feb92a5-86a7-4f86-aaa0-9b90d63cbfee"
        },
        "urlParams": {
            "productId": "1587",
            "quantity": "1",
            "fromDate": "20220110",
            "toDate": "20220210"
        }
    },
    "response": "",
    "context": {
        "errors": [
            {
                "field": "fromDate",
                "message": "start date should not be in the past"
            }
        ]
    }
}

correct_response = {
    "request": {
        "body": "",
        "query": {
            "5feb92a5-86a7-4f86-aaa0-9b90d63cbfee": "",
            "affiliateId": "londontheatredd"
        },
        "urlParams": {
            "productId": "1587",
            "quantity": "1",
            "fromDate": "20220317",
            "toDate": "20220317"
        }
    },
    "response": [
        {
            "datetime": "2022-03-17T19:30:00+0000",
            "partTwoDatetime": None,
            "largestLumpOfTickets": 9,
            "availableSeatCount": 636,
            "minPrice": 2500,
            "maxPrice": None,
            "noBookingFee": False,
            "discount": False,
            "promotionLabel": None
        }
    ],
    "context": None
}