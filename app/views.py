from django.shortcuts import render
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.db.models.deletion import ProtectedError
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from django.utils.decorators import method_decorator 

from .serializers import CategorySerializer, CardSerializer
from .models import Category, Card

import random
import json
from urllib import parse

class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, pk=None) :
        querySet = Category.objects.filter(id=pk)
        try :
            querySet.get()
            querySet.delete()
        except ObjectDoesNotExist :
            return HttpResponseServerError(reason="Object Does Not Exist.")
        except ProtectedError :
            return HttpResponseServerError(reason="Object is referenced by another model as a foreign key")

        return HttpResponse()

    @method_decorator(login_required(login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(CategoryViewSet, self).dispatch(*args, **kwargs)


class CardViewSet(viewsets.ModelViewSet) :
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @method_decorator(login_required(login_url='/admin/login'))
    def dispatch(self, *args, **kwargs) :
        return super(CardViewSet, self).dispatch(*args, **kwargs)


@login_required(login_url='/admin/login')
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
        
        if len(cards) == 0 :
            raise ObjectDoesNotExist("{}(id={}) category has no cards".format(randomCategory, categoryId)) # return 500
        else :
            randomCard = random.choice(list(cards))

        dictObject = model_to_dict(randomCard)
        serialized = json.dumps(dictObject)

        return HttpResponse(serialized)

    else :
        return HttpResponseNotAllowed(["GET"])


def isLoggedIn(request) :
    if request.user.is_authenticated :
        return HttpResponse()
    else :
        return HttpResponseRedirect(redirect_to='/admin/login/?next=/') # next=/, 메인으로 이동
