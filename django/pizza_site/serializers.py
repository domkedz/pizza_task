from rest_framework import serializers

from .models import Pizza, Topping


class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
        return value.name

    class Meta:
        model = Topping
        fields = ['name']


class CountToppings(serializers.Field):
    def to_representation(self, value):
        return value.count_toppings


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    topping = ToppingSerializer(many=True, read_only=True)
    count_toppings = CountToppings

    class Meta:
        model = Pizza
        fields = ['name', 'price', 'topping', 'count_toppings', 'rating']
