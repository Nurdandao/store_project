from django.urls import path
from .views import login, register, profile, email

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('email/', email, name='email'),
]