from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('home/', views.admin_view, name='admin'),
    path('', RedirectView.as_view(url = 'home/', permanent=True)),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adminstrative_auth/users/', views.user_table, name='user_table'),
    path('adminstrative_auth/grp/', views.grp_table, name='grp_table'),
    path('other/messages/', views.message_table, name='messages_table'),
    path('adminstrative_auth/', views.adminstration, name='adminstration')
]