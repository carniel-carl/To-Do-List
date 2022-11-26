from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("delete/<item_id>", views.deleteItem, name="deleteItem"),
    path("update/<item_id>", views.updateItem, name="updateItem"),
]