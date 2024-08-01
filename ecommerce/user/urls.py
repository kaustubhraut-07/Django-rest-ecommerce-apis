from django.urls import path
from .views import register , login , userpurchased


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('userpurchased/', userpurchased, name='userpurchased'),
]