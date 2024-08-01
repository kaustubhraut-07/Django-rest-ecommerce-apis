from django.urls import path
from .views import GetLatestProducts , ProductDetail , search , CreateProduct


urlpatterns = [
    path('latest-products/', GetLatestProducts.as_view()),
    path('search/', search, name='search'),
    # path('product/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('product/<slug:product_slug>/', ProductDetail.as_view()),
    # path('product/create/', CreateProduct.as_view() , name='createproduct'),
    path('create/', CreateProduct.as_view() , name='createproduct'),
    path('delete/<int:pk>/', CreateProduct.as_view() , name='deleteproduct'),
    path('update/<int:pk>/', CreateProduct.as_view() , name='updateproduct'),
]   