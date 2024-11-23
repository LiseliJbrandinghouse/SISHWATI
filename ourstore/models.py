from django.db import models
from django.utils import timezone
from datetime import timedelta

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('totes', 'Totes'),
        ('handbags', 'Handbags'),
        # Add more categories as needed
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shop/')  # Default image
    hover_image = models.ImageField(upload_to='shop/', blank=True, null=True)  # Secondary image for hover effect
    available_colors = models.JSONField(default=list)  # Store colors as a list of options
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='totes')  # Category field
    is_new_arrival = models.BooleanField(default=False)  # Is this a new arrival?
    is_out_of_stock = models.BooleanField(default=False)  # New field to mark as out of stock
    is_new_collection = models.BooleanField(default=False)  # New field
    is_new_launch = models.BooleanField(default=False)  # Marks a product as new launch
    launch_date = models.DateTimeField(default=timezone.now)  # Date and time for product launch
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def is_launched(self):
        # Check if the current date and time is after the launch date
        return timezone.now() >= self.launch_date

    def is_still_new(self):
        # Check if the product is still considered new (within a month from launch)
        return timezone.now() <= self.launch_date + timedelta(days=30)


    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    color = models.CharField(max_length=50)  # The color that this image corresponds to
    image = models.ImageField(upload_to='product_colors/')  # The image for that color

    def __str__(self):
        return f"{self.product.name} - {self.color}"