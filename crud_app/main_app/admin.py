from django.contrib import admin
from main_app.models import stock

# Register your models here.
# admin.site.register(stock)

@admin.register(stock)
class StockAdmin(admin.ModelAdmin):
    list_display =('trade_code','date')
        