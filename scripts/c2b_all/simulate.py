import requests
from keys import *
from access_token import generate_access_token


my_access_token = generate_access_token()

def simulate_c2b_transaction():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {"ShortCode": c2b_shortcode,
               "CommandID": "CustomerPayBillOnline",
               "Amount": "1",
               "Msisdn": msisnd,
               "BillRefNumber": "12345"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
