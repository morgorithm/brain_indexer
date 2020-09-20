from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .serializers import CategorySerializer, CardSerializer
from .models import Category, Card

class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CardViewSet(viewsets.ModelViewSet) :
    queryset = Card.objects.all()
    serializer_class = CardSerializer