from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import Category, ProductProvider, Stock, Transaction
from .serializers import (
    UserSerializer,
    CategorySerializer,
    ProductProviderSerializer,
    StockSerializer,
    TransactionSerializer,
)


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"


class ProductProviderList(generics.ListCreateAPIView):
    queryset = ProductProvider.objects.all()
    serializer_class = ProductProviderSerializer


class ProductProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductProvider.objects.all()
    serializer_class = ProductProviderSerializer
    lookup_field = "id"


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "id"


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"
