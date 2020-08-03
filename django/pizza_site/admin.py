from django.contrib import admin
from .models import Pizza, Topping


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating',)


class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
