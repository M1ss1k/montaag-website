from django import forms

from .models import LogisticsOrders

class Order(forms.ModelForm):

    class Meta:
        model = LogisticsOrders
        fields = ('name', 'order_contact', 'order_description', 'order_tariff', "order_to")
