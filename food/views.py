from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from rest_framework import status
from rest_framework import viewsets
from food.serializers import FoodListSerializer,FoodItemSerializer

class FoodView(viewsets.ViewSet):
	# -- Get list of all food items
	def get_food_list(self,request,format=None):
		try:
			food = Food.objects.all()
		except Food.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		food_serializer = FoodListSerializer(food,many=True)
		return Response(food_serializer.data)

	# -- Get list of individual items
	def get_food_item(self,request,pk,format=None):
		try:
			food = Food.objects.filter(id=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		food_serializer = FoodItemSerializer(food,many=True)
		return Response(food_serializer.data)
		



