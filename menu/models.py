from django.db import models

# Create your models here.
class Toppings(models.Model):
    item_name = models.CharField(max_length=64)

    def __str__(self):
        return f"Topping: {self.item_name}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return f"Category : {self.category_name}"

class Items(models.Model):
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Items")
    item_name = models.CharField(max_length=64)
    max_toppings = models.IntegerField(null=True)

    def __str__(self):
        return f"Item Category: {item_category} Name: {item_name} Max_toppings: {max_toppings}"

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
    
    