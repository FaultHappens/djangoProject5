from django.urls import path
from user.views import  register, login
urlpatterns = [
    path('register/', register),
    path('login/', login)
]