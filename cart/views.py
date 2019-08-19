from django.shortcuts import render
from .models import Cart
from django.conf import settings
from rest_framework.response import Response
from .serializers import CartSerializer,OrderItemSerializer
from .models import CartItem
from food.models import Food
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import status

class CartView(viewsets.ViewSet):
	# Add food item to cart -- Checked
	def add_item(self,request,format=None):
		checkout_body = request.data
		try:
			user_item = User.objects.get(id=checkout_body['user'])
			checkout_item = CartItem.objects.create(user=User.objects.get(id=int(checkout_body['user'])),
													item=Food.objects.get(id=int(checkout_body['item'])),
													quantity=checkout_body['quantity'],
													completed=False)
			checkout_item.save()
			return Response({"data":checkout_item.id},status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	# Checkout from cart -- Checked
	def checkout(self,request,pk,format=None):
		try:
			cart_item_update = CartItem.objects.filter(user=User.objects.get(id=self.kwargs.get("pk")),completed=False)
		except CartItem.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		cart_item_update.update(completed=True)
		cart_list  = Cart.objects.get_or_create(user=User.objects.get(id=self.kwargs.get("pk")))

		for cart_items in cart_item_update:
			cart_list.ordered_item.add(cart_items)
			CartItem.objects.filter(id=cart_items.id,user=User.objects.get(id=self.kwargs.get("pk"))).delete()
		#cart_list.save()
		serializer = CartSerializer(cart_list,many=True)
		return Response(serializer.data,status=status.HTTP_201_CREATED)
			
	# Get Order details 
	def get_order_list(self,request,pk,format=None):
		try:
			cart_item_list = Cart.objects.filter(user=User.objects.get(id=self.kwargs.get("pk")))
			serializer = CartSerializer(cart_item_list,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	 
	# Admin : Get all pending orders -- Checked
	def all_pending_orders(self,request,format=None):
		try:
			cart_item_list 	= Cart.objects.filter(completed='pending')
			serializer = CartSerializer(cart_item_list,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	# Mark orders as delivered -- Checked
	def remove_pending_orders(self,request,pk,format=None):
		try:
			cart_item_list = Cart.objects.filter(user=User.objects.get(id=self.kwargs.get("pk")),completed='pending',id=request.data.get('cart_id'))
			cart_item_list.update(completed='shipped')
			print(cart_item_list)
			serializer = CartSerializer(cart_item_list,many=True)
			return Response(serializer.data)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class CartItemList(viewsets.ViewSet):
	# View the cart status -- Checked
	def view_cart(self,request,pk,format=None):
		
		cart_items = CartItem.objects.filter(user=User.objects.get(id=self.kwargs.get("pk")))
		serializer = OrderItemSerializer(cart_items,many=True)
		return Response(serializer.data)

