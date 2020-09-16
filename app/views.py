from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Category


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.order_by('updated_at')
