# Generated by Django 2.1.8 on 2019-08-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20190818_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='completed',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped')], default='pending', max_length=120),
        ),
    ]
