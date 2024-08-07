from django.contrib import admin
from cars.models import Car, Brand


# Modelos para o site administrativo, os campos que aparecem lá
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
