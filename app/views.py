from django.shortcuts import render, get_object_or_404
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
    picked_category_names = request.GET.getlist('categories')
    if len(picked_category_names) == 0:
        print('No selected category')
        categories = Category.objects.order_by(('updated_at'))
        return render(request, 'index.html', {'categories': categories})

    picked_category_name = pick_randomly(picked_category_names)
    random_category = Category.objects.get(name=picked_category_name)
    cards = Card.objects.filter(category=random_category)

    if len(cards) == 0:
        print('No card found for the category ' + picked_category_name)
        categories = Category.objects.order_by(('updated_at'))
        return render(request, 'index.html', {'categories': categories})

    else:
        card = pick_randomly(cards)
        return render(request, 'brain_indexing.html', {'card': card})


def known_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)

    print(card)
    print('Count up the as known card')

    return brain_indexing(request)


def unknown_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)

    print(card)
    print('Count down as unkown card')

    return brain_indexing(request)


def pick_randomly(list):
    idx = random.randint(0, len(list) - 1)
    return list[idx]
