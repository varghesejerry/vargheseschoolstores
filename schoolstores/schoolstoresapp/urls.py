from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('register', views.register, name='register'),
    path('login', views.login,name='login'),
    path('order', views.order, name='order'),
    path('logout',views.logout,name='logout'),
    path('order_confirmation', views.order, name='order_confirmation'),
]