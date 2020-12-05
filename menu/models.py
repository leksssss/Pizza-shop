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
    SIZE_TYPES = (
        ('y','Yes'),
        ('n', 'Null')
    )
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='items')
    item_name = models.CharField(max_length=64)
    max_toppings = models.IntegerField(null=True)
    image = models.ImageField(upload_to="item_images/", default=' ')
    size_type = models.CharField(max_length=1, choices=SIZE_TYPES)
    small = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    large = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True)


    def __str__(self):
        if(self.size_type != 'n'):
            return f"Item Category: {self.category_name} Name: {self.item_name} Small: ${self.small} Large : ${self.large} Max_toppings: {self.max_toppings}"
        else:
            return f"Item Category: {self.category_name} Name: {self.item_name} Price: ${self.price} Max_toppings: {self.max_toppings}"
        

      
    
    