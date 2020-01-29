from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.http import JsonResponse

from mpesa.api.serializers import LNMOnlineSerializer, C2BPaymentsSerializer
from mpesa.models import LNMOnline, C2BPayments

from datetime import datetime
import pytz

from scripts.lipanampesa import lipa_na_mpesa
from scripts.c2b_all.register import register_url
from scripts.c2b_all.simulate import simulate_c2b_transaction

class LNMCallbackUrlApiView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data) 

        """
        Callback url response

        {'Body': 
            {'stkCallback': 
               {
                    'MerchantRequestID': '21301-7887811-1', 
                    'CheckoutRequestID': 'ws_CO_260120201833093897', 
                    'ResultCode': 0, 
                    'ResultDesc': 'The service request is processed successfully.', 
                    'CallbackMetadata':
                        {'Item': 
                            [
                                {'Name': 'Amount', 'Value': 2.0}, 
                                {'Name': 'MpesaReceiptNumber', 'Value': 'OAQ6MVQHHI'}, 
                                {'Name': 'Balance'},
                                {'Name': 'TransactionDate', 'Value': 20200126183321}, 
                                {'Name': 'PhoneNumber', 'Value': 254712115461}
                            ]
                        }
                }
            }   
        }
        """

        stkCallback = request.data['Body']['stkCallback']
        merchant_request_id = stkCallback['MerchantRequestID']
        checkout_request_id = stkCallback['CheckoutRequestID']
        result_code  = stkCallback['ResultCode']
        result_desc  = stkCallback['ResultDesc']
        amount = stkCallback['CallbackMetadata']['Item'][0]['Value']
        mpesa_receipt_number = stkCallback['CallbackMetadata']['Item'][1]['Value']
        balance = ''
        transaction_date = stkCallback['CallbackMetadata']['Item'][3]['Value']
        phonenumber = stkCallback['CallbackMetadata']['Item'][4]['Value']

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
        return Response('Success!')


class C2BConfirmationApiView(CreateAPIView):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentsSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data, ': Data from Confirmation')
            
        transaction_time = request.data['TransTime']
        str_transaction_date = str(transaction_time)
        transaction_date = datetime.strptime(str_transaction_date, '%Y%m%d%H%M%S')
        #Sync Safaricoms response time with server time
        aware_transaction_date = pytz.utc.localize(transaction_date)
        print(aware_transaction_date)

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
            TransactionType = transaction_type,
            TransID = transaction_id,
            TransTime = transaction_time,
            TransAmount = transaction_amount,
            BusinessShortCode = business_short_code,
            BillRefNumber = bill_ref_number,
            InvoiceNumber = invoice_number,
            OrgAccountBalance = org_account_balance,
            ThirdPartyTransID = third_party_transaction_id,
            MSISDN = phone_number,
            FirstName = first_name,
            MiddleName = middle_name,
            LastName = last_name,
        )

        c2bmodel_data.save()
        c2b_data = C2BPayments.objects.all()
        data = C2BPaymentsSerializer(c2b_data, many=True)
        c2b_context = {
            "Result Code": 0,
            "Data": data
        }


        return Response(c2b_context)


# @permission_classes([IsAuthenticated])
class MakeLNMPayment(ModelViewSet):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        phonenumber = self.request.query_params.get('phone_number')
        amount = self.request.query_params.get('amount')

        payment = lipa_na_mpesa(phonenumber, amount)
        print(payment)
        return super().get_queryset()


class MakeC2BPayment(ModelViewSet):
    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        register_url()

        phonenumber = self.request.query_params.get('phone_number')
        amount = self.request.query_params.get('amount')

        payment = simulate_c2b_transaction(phonenumber, amount)
        print(payment)
        return super().get_queryset()
