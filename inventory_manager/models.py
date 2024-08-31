from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    in_stock = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    TransactionType = [
        ("Purchase", "purchase"),
        ("Sale", "sale"),
    ]

    transaction_type = models.CharField(max_length=30, choices=TransactionType)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
