# Generated by Django 2.1.8 on 2019-08-18 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_remove_cart_number_of_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='completed',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped')], default='created', max_length=120),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='completed',
            field=models.BooleanField(default=False, max_length=120),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart',
            name='ordered_item',
            field=models.ManyToManyField(to='cart.CartItem'),
        ),
    ]