from django.urls import path
from . import views

urlpatterns = [
    path('lizts', views.lizt_list, name='lizt_list'),
    path('lizts/<int:pk>', views.lizt_detail, name='lizt_detail'),
    path('lizts/new', views.lizt_create, name='lizt_create'),
    path('lizts/<int:pk>/delete', views.lizt_delete, name='lizt_delete'),

    path('items', views.item_list, name='item_list'),
    path('items/new', views.item_create, name='item_create'),
    path('items/<int:pk>', views.item_detail, name='item_detail'),

]