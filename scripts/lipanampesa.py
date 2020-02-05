import requests
from datetime import datetime
from decouple import config, Csv
from scripts.keys import *
from scripts.access_token import generate_access_token
from scripts.utils import generate_timestamp
from scripts.password import generate_password
from decouple import Csv, config

# Execute all functions
formatted_time = generate_timestamp()
password = generate_password(formatted_time)
my_access_token = generate_access_token()


def lipa_na_mpesa(phonenumber, amount):
    print('Start excecuting the Simulate LNMOnline function:::')
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": config('BusinessShortCode'),
        "Password": password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phonenumber,
        "PartyB": config('BusinessShortCode'),
        "PhoneNumber":phonenumber,
        "CallBackURL": config('LNM_CALLBACK_URL'),
        "AccountReference": "vicks_test",
        "TransactionDesc": "Pay for internet"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    return response.text
    
