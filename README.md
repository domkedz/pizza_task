# Pizza task #

----
Write a backend part of a web application in python, which will allow voting for the best pizza.

Application must track the amount of toppings on each pizza.

Voting should be available via REST API.


# Create superuser


python manage.py createsuperuser --email admin@example.com --username admin

The Django admin can be used to add specific pizzas and toppings.


# GET


pizzas/ endpoint returns all saved pizzas with their name, price, toppings and count of toppings.


toppings/ endpoint returns all saved toppings


# POST


vote/id endpoint can be used to vote for pizza by id


# Running tests


docker exec -it pizza_web bash


python manage.py test pizza_site.tests
