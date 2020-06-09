from django import forms
from .models import Lizt, Item

class LiztForm(forms.ModelForm):
    class Meta:
        model = Lizt
        fields = ('title',)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('lizt', 'lizt_item', 'quantity',)
