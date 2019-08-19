from django.urls import path,include
from .views import CartView,CartItemList

urlpatterns = [
    path("cart/<int:pk>/", CartItemList.as_view({'get': 'view_cart'}), name="view_cart"),
    path("cart/<int:pk>", CartView.as_view({'post': 'remove_pending_orders'}), name="remove_pending_orders"),
    path("cart/", CartView.as_view({'post': 'add_item'}), name="add_item"),
    path("cart/pending/", CartView.as_view({'get': 'all_pending_orders'}), name="all_pending_orders"),
    path("order/<int:pk>", CartView.as_view({'get': 'get_order_list'}), name="get_order_list"),
    path("cart/checkout/<int:pk>", CartView.as_view({'get': 'checkout'}), name="checkout"),
]