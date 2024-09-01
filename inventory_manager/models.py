from django.db import models


class ProductProvider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(ProductProvider, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product.name


class Transaction(models.Model):
    TransactionType = [
        ("Purchase", "Purchase"),
        ("Sale", "Sale"),
    ]

    transaction_type = models.CharField(max_length=30, choices=TransactionType)
    product = models.ForeignKey(ProductProvider, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
