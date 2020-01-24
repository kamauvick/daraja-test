from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)


@admin.register(LNMOnline)
class LNMOnline(admin.ModelAdmin):

    list_display = ('id',
                    'phonenumber',
                    'amount',
                    'mpesa_receipt_number',
                    'transaction_date',
                     )

    list_filter = ('id', 'phonenumber', 'mpesa_receipt_number',)

    ordering = ("id", 'transaction_date',)

