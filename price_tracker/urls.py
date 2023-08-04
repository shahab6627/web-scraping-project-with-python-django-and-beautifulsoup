from .views import *

from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('register', userRegistration, name="register"),
    path('login', loginUser, name='login'),
    path('profile', profile, name='profile'),
    path('logout', logoutuser, name="logout"),
    path('update', updateItems, name="updateitems"),
    path('delete/<int:id>', deleteItem, name='delete')
]
