from django.db import models
from django.conf import settings
from food.models import Food
User = settings.AUTH_USER_MODEL

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
)
class Cart(models.Model):
	user         = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
	ordered_item = models.ManyToManyField("CartItem")
	updated      = models.DateTimeField(auto_now=True)
	timestamp    = models.DateTimeField(auto_now_add=True)
	completed    = models.CharField(max_length=120, default='pending', choices=ORDER_STATUS_CHOICES)

class CartItem(models.Model):
	user        = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
	item 		= models.ForeignKey(Food,on_delete=models.CASCADE)
	quantity 	= models.PositiveIntegerField(default=1)
	completed   = models.BooleanField(max_length=120, blank=False,default=False)

	



