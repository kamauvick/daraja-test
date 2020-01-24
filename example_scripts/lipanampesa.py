import requests
from datetime import datetime
from decouple import config, Csv
from keys import *
from access_token import generate_access_token
from utils import generate_timestamp
from password import generate_password

# Excecute all functions

formatted_time = generate_timestamp()
password = generate_password(formatted_time)
my_access_token = generate_access_token()


def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": config('BusinessShortCode'),
        "Password": password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": config('PhoneNumber'),
        "PartyB": config('BusinessShortCode'),
        "PhoneNumber": config('PhoneNumber'),
        "CallBackURL": "https://darajavick.herokuapp.com/api/payments/lnm/",
        "AccountReference": "12345678",
        "TransactionDesc": "Pay for internet"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    print (response.text)
    
lipa_na_mpesa()
