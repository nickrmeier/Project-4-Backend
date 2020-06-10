from rest_framework import generics
from .serializers import LiztSerializer, ItemSerializer
from .models import Lizt, Item

class LiztList(generics.ListCreateAPIView):
    queryset = Lizt.objects.all()
    serializer_class = LiztSerializer

class LiztDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lizt.objects.all()
    serializer_class = LiztSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer