# Generated by Django 3.0.8 on 2020-08-25 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_category_items_pricing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='item_name',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Pricing',
        ),
    ]