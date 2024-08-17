from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_view, name='admin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_table, name='user_table'),
    path('grp/', views.grp_table, name='grp_table'),
    path('messages/', views.message_table, name='messages_table')
]