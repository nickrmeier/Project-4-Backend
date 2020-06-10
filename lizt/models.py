from django.db import models

class Lizt(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Item(models.Model):
    lizt = models.ForeignKey(Lizt, on_delete=models.CASCADE, related_name='items')
    lizt_item = models.CharField(max_length=100, default='no items')
    quantity = models.CharField(max_length=10, default='0')
    def __str__(self):
        return 'name='+self.lizt_item+', quantity='+self.quantity