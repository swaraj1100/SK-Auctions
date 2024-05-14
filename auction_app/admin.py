from django.contrib import admin
from.models import product
from .models import Bid
# Register your models here.

admin.site.register(product)
class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'bid_amount', 'mobile', 'timestamp')
    search_fields = ('user__username', 'product__name', 'mobile')
    list_filter = ('product', 'timestamp')

admin.site.register(Bid, BidAdmin)