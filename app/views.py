from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from .models import Category, Card, CardDetail
import random


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.order_by('updated_at')


def brain_indexing(request):
    picked_category_name = pick_randomly(request.GET.getlist('categories'))
    random_category = Category.objects.filter(
        name=picked_category_name)
    print(random_category)

    card = pick_randomly(Card.objects.filter(category=random_category).count())

    return render(request, 'brain_indexing.html', {'card': card})


def pick_randomly(dict):
    idx = random.randint(0, len(dict) - 1)
    return dict[idx]
