from django.urls import path
from . import views

urlpatterns = [
    path('category/read', views.category_read, name='category_read'),
    path('category/create', views.category_create, name='category_create'),
    path('category/update', views.category_update, name='category_update'),
    path('category/delete', views.category_delete, name='category_delete'),


]