from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('validate_signup/', views.validate_signup, name = 'validate_signup'),
    path('validate_login/', views.validate_login, name = 'validate_login'),
]
