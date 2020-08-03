from django.db import models
from django.utils.translation import ugettext_lazy as _


class Topping(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name=_('name'))

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name=_('name'))
    price = models.FloatField(null=False, blank=False)
    topping = models.ManyToManyField(Topping, verbose_name=_('topping'))
    rating = models.IntegerField(verbose_name=_('rating'), default=0, null=False, blank=False)

    @property
    def count_toppings(self):
        return self.topping.all().count()
