from rest_framework import serializers
from mpesa.models import LNMOnline, C2BPayments

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = (
            'id', 
            'merchant_request_id', 
            'checkout_request_id',
            'result_code',
            'result_desc',
            'amount',
            'mpesa_receipt_number',
            'balance',
            'transaction_date',
            'phonenumber', )


class C2BPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = (
            'id',
            'transaction_type',
            'transaction_id',
            'transaction_time',
            'transaction_amount',
            'business_short_code',
            'bill_ref_number',
            'invoice_number',
            'org_account_balance',
            'third_party_transaction_id',
            'phone_number',
            'first_name',
            'middle_name',
            'last_name',
            )
