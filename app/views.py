from django.shortcuts import render
from django.core import serializers
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

        # choose random one
        randomCategory = random.choice(categories)
        # get category's id
        categoryId = Category.objects.get(name=randomCategory).id
        card = Card.objects.filter(category=categoryId)
        
        '''
        여기서 랜덤으로 한번 더 골라야 함
        데이터 여러 개 넣고 테스트해보기
        '''

        return HttpResponse(serializers.serialize('json', card), content_type="text/json-comment-filtered")
    else :
        return HttpResponseNotAllowed(["GET"])