from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('aboutus', views.about, name = 'aboutus'),
    path('melo', views.melo, name = 'melo'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('home', views.home, name = 'home'),
    path('profile', views.profile, name = 'profile'),
    path('novinki', views.novinki, name = 'novinki'),
    path('create', views.create, name='create')
]