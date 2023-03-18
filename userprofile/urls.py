from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]