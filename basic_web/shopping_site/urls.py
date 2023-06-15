from shopping_site.views import ProductView,AllProductView
from django.urls import path


urlpatterns = [
    path('product/<str:product_name>/', ProductView.as_view()),
    path('product',AllProductView.as_view())
]
