from rest_framework import serializers
from .models import Category, Card

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Card
        fields = '__all__'