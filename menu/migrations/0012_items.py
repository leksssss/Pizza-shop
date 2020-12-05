# Generated by Django 3.0.8 on 2020-12-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=64)),
                ('max_toppings', models.IntegerField(null=True)),
                ('image', models.ImageField(default=' ', upload_to='item_images/')),
                ('size_type', models.CharField(choices=[('y', 'Yes'), ('n', 'Null')], max_length=1)),
                ('small', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('large', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.Category')),
            ],
        ),
    ]