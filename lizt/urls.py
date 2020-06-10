from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('lizts/', views.LiztList.as_view(), name='lizt_list'),
    path('lizts/<int:pk>', views.LiztDetail.as_view(), name='lizt_detail'),
    path('items/', views.ItemList.as_view(), name="item_list"),
    path('Item/<int:pk>', views.ItemDetail.as_view(), name="item_detail")
]