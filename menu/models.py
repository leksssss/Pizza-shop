from django.db import models

# Create your models here.
class Toppings(models.Model):
    item_name = models.CharField(max_length=64)

    def __str__(self):
        return f"Topping: {self.item_name}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="category_images/", default=' ')
    def __str__(self):
        return f"Category : {self.category_name}"

class Items(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='items')
    item_name = models.CharField(max_length=64)
    max_toppings = models.IntegerField(null=True)
    image = models.ImageField(upload_to="item_images/", default=' ')

    def __str__(self):
        return f"Item Category: {self.category_name} Name: {self.item_name} Max_toppings: {self.max_toppings}"

class Pricing(models.Model):
    SIZE_TYPES = (
        ('s', 'Small'),
        ('l', 'Large'),
        ('n', 'Null')
    )
    item_name = models.ForeignKey(Items, on_delete= models.CASCADE)
    size_type = models.CharField(max_length=1, choices=SIZE_TYPES)
    price = models.DecimalField(max_digits=2,decimal_places=2)

    def __str__(self):
        if(size_type != 'n'):
            return f"Name: {self.item_name} Type: {self.size_type} Price: ${self.price}"
        else:
            return f"Name: {self.item_name} Price: ${self.price}"
    
    