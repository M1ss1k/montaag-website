from django.contrib import admin

from .models import LogisticsTariffs, LogisticsOrders

class LogisticsTariffsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')
    list_filter = ('title', 'price', 'description')
    search_fields = ('title', 'price')
class LogisticsOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_contact', 'order_tariff','order_time')
    list_filter = ('name', 'order_contact', 'order_tariff', 'order_time')
    search_fields = ('name', 'order_contact')

admin.site.register(LogisticsTariffs, LogisticsTariffsAdmin)
admin.site.register(LogisticsOrders, LogisticsOrderAdmin)
# Register your models here.
