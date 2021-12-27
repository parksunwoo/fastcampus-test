from django.urls import path, include
from order import views

urlpatterns = [
    path('shops/', views.shop),
    path('menus/<int:shop>', views.menu, name='menu'),
    path('order/', views.order, name='order'),
]
