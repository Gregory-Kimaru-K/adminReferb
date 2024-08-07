from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_view, name='admin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
