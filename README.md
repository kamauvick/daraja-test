# daraja-test
Test working with safaricom daraja api's


## Lipa na mpesa online

> Requirements:
* Consumer key and Consumer secret
* Test Credentials
    * LNM Business Shortcode
    * LNM Online Passkey
* Access token (Consumer key + Consumer Secret)
* Transaction Params
    * password (timestamp + LNM Business Shortcode + LNM Online Passkey)
    * timestamp
    * shortcode
    * account reference
    * phone number
    * amount

## C2B 
> Requirements
* A pair of urls for the paybill
    * Validation url
    * Confirmation url
* Access token (Consumer key + Consumer Secret)
* Transaction params

    > Register_url
    * Shortcode
    * ResponseType
    * ConfirmationURL
    * ValidationURL

    > Simulate_c2b_transaction
    * ShortCode
    * CommandID
    * Amount    
    * Msisdn
    * BillRefNumber