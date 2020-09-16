from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('brain_indexing', views.brain_indexing, name='brain_indexing')
]
