# Generated by Django 4.0.5 on 2022-06-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_category_item_lable'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=()),
        ),
    ]