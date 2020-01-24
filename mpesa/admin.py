from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)


@admin.register(LNMOnline)
class LNMOnline(admin.ModelAdmin):

    list_display = ('id',
                    'merchant_request_id',
                    'checkout_request_id',
                    'result_code',
                    'result_desc',
                    'amount',
                    'mpesa_receipt_number',
                    'balance',
                    'transaction_date',
                    'phonenumber', )

    list_filter = ('id', 'phonenumber', 'mpesa_receipt_number',)

    ordering = ("id", 'transaction_date',)

