import requests
from keys import *
from access_token import generate_access_token

my_access_token = generate_access_token()

def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {"ShortCode": c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://vickecommerce.com/confirmation",
               "ValidationURL": "https://vickecommerce.com/validation_url"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)
