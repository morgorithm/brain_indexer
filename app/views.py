from django.shortcuts import render
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .serializers import CategorySerializer, CardSerializer
from .models import Category, Card

import random

class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CardViewSet(viewsets.ModelViewSet) :
    queryset = Card.objects.all()
    serializer_class = CardSerializer

def getRandomCard(request) :
    if request.method == 'GET' :
        categories = request.GET.get('category')
        if categories is None :
            return HttpResponseBadRequest()
        categories = categories.split(',')

        # choose random category
        randomCategory = random.choice(categories)
        
        # get category's id
        try :
            categoryId = Category.objects.get(name=randomCategory).id
        except ObjectDoesNotExist :     
            return HttpResponseBadRequest("there's no category : {}".format(randomCategory))

        cards = Card.objects.filter(category=categoryId)
        randomCard = random.choice(list(cards))

        return HttpResponse(serializers.serialize('json', [randomCard]), content_type="text/json-comment-filtered")
    else :
        return HttpResponseNotAllowed(["GET"])