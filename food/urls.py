from django.urls import path,include
from .views import FoodView
urlpatterns = [
    path("food/", FoodView.as_view({'get': 'get_food_list'}), name="get_menu"),
    path("food/<int:pk>",
    	FoodView.as_view({'get': 'get_food_item'}),
    	name='get_food_item',
    ),
]