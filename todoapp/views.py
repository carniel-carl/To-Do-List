from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

from .forms import *


# Create your views here.

def index(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ITEM ADDED SUCCESSFULLY")
        return redirect("index")

    todo = Item.objects.all()

    context = {"items": todo, "form": form}
    return render(request, "index.html", context)


def deleteItem(request, item_id):
    item_to_delete = Item.objects.get(pk=item_id)
    item_to_delete.delete()
    messages.error(request, "ITEM DELECTED")

    return redirect("index")


def updateItem(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"form": form}
    return render(request, "edit.html", context)


def register(request):
    return render(request, 'register.html')
