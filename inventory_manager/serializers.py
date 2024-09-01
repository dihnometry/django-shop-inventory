from rest_framework import serializers
from .models import Category, ProductProvider, Stock, Transaction


class ProductProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProvider
        fields = ["id", "name", "description", "price"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            "id",
            "product",
            "quantity",
            "category",
            "creation_date",
            "update_date",
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "transaction_type",
            "product",
            "quantity",
            "total_price",
            "transaction_date",
        ]

    def create(self, validated_data):
        transaction_type: str = validated_data.get("transaction_type")
        product = validated_data.get("product")
        quantity = validated_data.get("quantity")

        if transaction_type == "Purchase":
            stock, _ = Stock.objects.get_or_create(
                product=product, defaults={"quantity": 0}
            )
            stock.quantity += quantity
            stock.save()

        if transaction_type == "Sale":
            stock = Stock.objects.get(product=product)
            if stock.quantity < quantity:
                raise serializers.ValidationError(
                    "No hay suficiente stock para realizar la venta."
                )

            stock.quantity -= quantity
            stock.save()

        transaction = Transaction.objects.create(**validated_data)
        return transaction
