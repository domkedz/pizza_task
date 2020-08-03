from .models import Pizza, Topping
from .serializers import PizzaSerializer, ToppingSerializer
from rest_framework import viewsets
from rest_framework import views
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class PizzasViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class ToppingsViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class PizzaVoteViewSet(views.APIView):

    def post(self, request, pk=None, format=None):
        try:
            pizza = Pizza.objects.get(id=pk)
        except ObjectDoesNotExist:
            return HttpResponse("Pizza not found!", status=404)
        pizza.rating += 1
        pizza.save()
        return HttpResponse(status=200)
