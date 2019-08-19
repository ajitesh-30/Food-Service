from django.db import models

# Create your models here.

class Food(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
	description = models.TextField(default=None)

	def __str__(self):
		return self.name





