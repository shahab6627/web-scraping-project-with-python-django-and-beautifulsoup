from django.contrib import admin
from .models import ItmePrice
# Register your models here.


class ItmePriceModel(admin.ModelAdmin):
    list_display = ('item_title', 'current_price','old_price','price_difference','user')

    def save_model(self, request, obj, form, change):
            if not obj.user:
                obj.user = request.user
            obj.save()


admin.site.register(ItmePrice, ItmePriceModel)