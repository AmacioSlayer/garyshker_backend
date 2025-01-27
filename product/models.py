from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    vendor = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.vendor