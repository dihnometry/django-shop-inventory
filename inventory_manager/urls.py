from django.urls import path

from . import views

urlpatterns = [
    path("api/categories", views.CategoryList.as_view()),
    path("api/categories/<int:id>", views.CategoryDetail.as_view()),
    path("api/products", views.ProductProviderList.as_view()),
    path("api/products/<int:id>", views.ProductProviderDetail.as_view()),
    path("api/stock", views.StockList.as_view()),
    path("api/stock/<int:id>", views.StockDetail.as_view()),
    path("api/transactions", views.TransactionList.as_view()),
    path("api/transactions/<int:id>", views.TransactionDetail.as_view()),
]
