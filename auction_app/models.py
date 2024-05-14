from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    img = models.ImageField(upload_to="gallery")
    name = models.CharField(max_length=250)
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)  # Assuming Product is the correct model name
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    mobile = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - ₹{self.bid_amount}"

