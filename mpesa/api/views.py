from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse

from mpesa.api.serializers import LNMOnlineSerializer, C2BPaymentsSerializer
from mpesa.models import LNMOnline, C2BPayments

from datetime import datetime
import pytz

class LNMCallbackUrlApiView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data) 
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code  = request.data['Body']['stkCallback']['ResultCode']
        result_desc  = request.data['Body']['stkCallback']['ResultDesc']
        amount = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        mpesa_receipt_number = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        balance = ''
        transaction_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][2]['Value']
        phonenumber = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']

        str_transaction_date = str(transaction_date)
        transaction_date = datetime.strptime(str_transaction_date, '%Y%m%d%H%M%S')

        #Sync Safaricoms response time with server time
        aware_transaction_date = pytz.utc.localize(transaction_date)

        mpesa_model_data = LNMOnline.objects.create(
            merchant_request_id = merchant_request_id,
            checkout_request_id = checkout_request_id,
            result_code = result_code,
            result_desc = result_desc,
            amount = amount,
            mpesa_receipt_number = mpesa_receipt_number,
            balance = balance,
            transaction_date = aware_transaction_date,
            phonenumber = phonenumber,
        )
        
        mpesa_model_data.save()

        transaction_data = LNMOnline.objects.all()
        response_data = LNMOnlineSerializer(transaction_data, many=True)

        return Response(response_data.data)


class C2BValidationApiView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentsSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data , ': Data from validation')
        transaction_time = request.data['TransTime']
        str_transaction_date = str(transaction_time)
        transaction_date = datetime.strptime(str_transaction_date, '%Y%m%d%H%M%S')
        #Sync Safaricoms response time with server time
        aware_transaction_date = pytz.utc.localize(transaction_date)

        transaction_type = request.data['TransactionType']
        transaction_id = request.data['TransID']
        transaction_time = aware_transaction_date
        transaction_amount = request.data['TransAmount']
        business_short_code = request.data['BusinessShortCode']
        bill_ref_number = request.data['BillRefNumber']
        invoice_number = request.data['InvoiceNumber']
        org_account_balance = request.data['OrgAccountBalance']
        third_party_transaction_id = request.data['ThirdPartyTransID']
        phone_number = request.data['MSISDN']
        first_name = request.data['FirstName']
        middle_name = request.data['MiddleName']
        last_name = request.data['LastName']

        c2bmodel_data = C2BPayments.objects.create(
            transaction_type = transaction_type,
            transaction_id = transaction_id,
            transaction_time = transaction_time,
            transaction_amount = transaction_amount,
            business_short_code = business_short_code,
            bill_ref_number = bill_ref_number,
            invoice_number = invoice_number,
            org_account_balance = org_account_balance,
            third_party_transaction_id = third_party_transaction_id,
            phone_number = phone_number,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,

        )

        c2bmodel_data.save()
        return Response('Success!')


class C2BConfirmationApiView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentsSerializer
    permission_classes = [AllowAny]

    # def create(self, request):
    #     print(request.data, ': Data from Confirmation')

    #     transaction_time = request.data['TransTime']
    #     str_transaction_date = str(transaction_time)
    #     transaction_date = datetime.strptime(str_transaction_date, '%Y%m%d%H%M%S')
    #     #Sync Safaricoms response time with server time
    #     aware_transaction_date = pytz.utc.localize(transaction_date)

    #     transaction_type = request.data['TransactionType']
    #     transaction_id = request.data['TransID']
    #     transaction_time = aware_transaction_date
    #     transaction_amount = request.data['TransAmount']
    #     business_short_code = request.data['BusinessShortCode']
    #     bill_ref_number = request.data['BillRefNumber']
    #     invoice_number = request.data['InvoiceNumber']
    #     org_account_balance = request.data['OrgAccountBalance']
    #     third_party_transaction_id = request.data['ThirdPartyTransID']
    #     phone_number = request.data['MSISDN']
    #     first_name = request.data['FirstName']
    #     middle_name = request.data['MiddleName']
    #     last_name = request.data['LastName']

    #     c2bmodel_data = C2BPayments.objects.create(
    #         transaction_type = transaction_type,
    #         transaction_id = transaction_id,
    #         transaction_time = transaction_time,
    #         transaction_amount = transaction_amount,
    #         business_short_code = business_short_code,
    #         bill_ref_number = bill_ref_number,
    #         invoice_number = invoice_number,
    #         org_account_balance = org_account_balance,
    #         third_party_transaction_id = third_party_transaction_id,
    #         phone_number = phone_number,
    #         first_name = first_name,
    #         middle_name = middle_name,
    #         last_name = last_name,

    #     )

    #     c2bmodel_data.save()
        # return Response({'Result_Desc': 0})
