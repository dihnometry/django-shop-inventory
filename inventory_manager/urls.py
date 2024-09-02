from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("api/token", TokenObtainPairView.as_view()),
    path("api/token/refresh", TokenRefreshView.as_view()),
    path("api/users", views.UserList.as_view()),
    path("api/users/<int:id>", views.UserDetail.as_view()),
    path("api/categories", views.CategoryList.as_view()),
    path("api/categories/<int:id>", views.CategoryDetail.as_view()),
    path("api/products", views.ProductProviderList.as_view()),
    path("api/products/<int:id>", views.ProductProviderDetail.as_view()),
    path("api/stock", views.StockList.as_view()),
    path("api/stock/<int:id>", views.StockDetail.as_view()),
    path("api/transactions", views.TransactionList.as_view()),
    path("api/transactions/<int:id>", views.TransactionDetail.as_view()),
]
