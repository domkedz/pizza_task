from pizza_site import views
from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'pizzas', views.PizzasViewSet)
router.register(r'toppings', views.ToppingsViewSet)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('vote/<int:pk>', views.PizzaVoteViewSet.as_view()),
    path('', include(router.urls)),
]
