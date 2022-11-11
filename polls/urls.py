from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.singup, name='signup',),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]