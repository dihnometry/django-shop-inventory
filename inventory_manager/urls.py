from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("token", TokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
    path("users", views.UserList.as_view()),
    path("users/<int:id>", views.UserDetail.as_view()),
    path("categories", views.CategoryList.as_view()),
    path("categories/<int:id>", views.CategoryDetail.as_view()),
    path("products", views.ProductProviderList.as_view()),
    path("products/<int:id>", views.ProductProviderDetail.as_view()),
    path("stock", views.StockList.as_view()),
    path("stock/<int:id>", views.StockDetail.as_view()),
    path("transactions", views.TransactionList.as_view()),
    path("transactions/<int:id>", views.TransactionDetail.as_view()),
]
