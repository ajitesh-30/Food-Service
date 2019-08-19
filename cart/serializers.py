from rest_framework import serializers
from .models import Cart,CartItem
from food.models import Food
from food.serializers import FoodItemSerializer
from django.conf import settings
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username')
class OrderItemSerializer(serializers.ModelSerializer):
	item=FoodItemSerializer(read_only=True)
	class Meta:
		model=CartItem
		fields='__all__'

class CartSerializer(serializers.ModelSerializer):
	ordered_item=OrderItemSerializer(read_only=True,many=True)	
	class Meta:
		model = Cart
		fields = '__all__'

