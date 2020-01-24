from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse

from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline

from datetime import datetime
import pytz

class LNMCallbackUrlApiView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
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
