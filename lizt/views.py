from django.shortcuts import render, redirect
from .models import Lizt, Item
from .forms import LiztForm, ItemForm


# LIZT

#GET all
def lizt_list(request):
    lizts = Lizt.objects.all()
    return render(request, 'lizt/lizt_list.html', {'lizts': lizts})

# GET detail
def lizt_detail(request, pk):
    lizt = Lizt.objects.get(id=pk)
    return render(request, 'lizt/lizt_detail.html', {'lizt': lizt})

# POST
def lizt_create(request):
    if request.method == 'POST':
        form = LiztForm(request.POST)
        if form.is_valid():
            lizt = form.save()
            return redirect('lizt_detail', pk=lizt.pk)
    else:
        form = LiztForm()
    return render(request, 'lizt/lizt_form.html', {'form': form})

def lizt_delete(request, pk):
    Lizt.objects.get(id=pk).delete()
    return redirect('lizt_list')


# ITEM

#GET all
def item_list(request):
    items = Item.objects.all()
    return render(request, 'lizt/item_list.html', {'items': items})

def item_detail(request, pk):
    items = item.objects.get(id=pk)
    return render(request, 'lizt/item_detail.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            items = form.save()
            return redirect('lizt_detail')

    else:
        form = ItemForm()
    return render(request, 'lizt/item_form.html', {'form': form})