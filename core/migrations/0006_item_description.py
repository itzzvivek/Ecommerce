# Generated by Django 4.0.5 on 2022-06-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test descriptions lorem'),
            preserve_default=False,
        ),
    ]
