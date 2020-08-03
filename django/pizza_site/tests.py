from django.test import TestCase
from .models import Pizza, Topping
from rest_framework.test import APIClient


class PizzaTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.topping1 = Topping.objects.create(name='Tomato')
        self.topping2 = Topping.objects.create(name='Cheese')
        self.topping3 = Topping.objects.create(name='Salami')
        self.pizza1 = Pizza.objects.create(name='Margherita', price=12,)
        self.pizza1.topping.add(self.topping1, self.topping2)
        self.pizza2 = Pizza.objects.create(name='Salami', price=14)
        self.pizza2.topping.add(self.topping1, self.topping2, self.topping3)

    def test_count_of_toppings(self):
        count1 = self.pizza1.topping.count()
        count2 = self.pizza2.topping.count()
        self.assertEqual(self.pizza1.count_toppings, count1)
        self.assertEqual(self.pizza2.count_toppings, count2)

    def test_vote_pizza1(self):
        response = self.client.post('/vote/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Pizza.objects.get(id=1).rating, 1)
        response = self.client.post('/vote/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Pizza.objects.get(id=1).rating, 2)

    def test_vote_pizza2(self):
        self.assertEqual(Pizza.objects.get(id=2).rating, 0)
