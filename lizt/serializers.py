from rest_framework import serializers
from .models import Lizt, Item

class LiztSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(
        many=True,
        read_only=True
    )
    class Meta: 
        model = Lizt
        fields = ('id', 'title', 'items',)

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    lizt = serializers.HyperlinkedRelatedField(
        view_name='lizt_detail',
        read_only=True
    )
    class Meta: 
        model = Item
        fields = ('id', 'lizt', 'lizt_item', 'quantity',)