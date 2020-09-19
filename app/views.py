from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from .query import *
from .forms import *

# Create your views here.

# category/read
@csrf_exempt
def category_read(request) :
    if request.method == 'POST' :
        form = CategoryForm(request.POST)
        if form.data :
            name = form.data['name']
            data = CategoryQuery().readCategory(name)
        else :
            data = CategoryQuery().readCategory()
            
        json = serializers.serialize('json', data)
        return HttpResponse(json, content_type="text/json-comment-filtered")
    elif request.method == 'GET' :
        return HttpResponseNotAllowed(['POST'])

# category/create
@csrf_exempt
def category_create(request) :
    if request.method == 'POST' :
        form = CategoryForm(request.POST)
        if form.data :
            name = form.data['name']
            return HttpResponse(CategoryQuery().createCategory(name))
        else :
            return HttpResponseServerError()
    elif request.method == 'GET' :
        return HttpResponseNotAllowed(['POST'])

# category/update
@csrf_exempt
def category_update(request) :
    if request.method == 'POST' :
        form = CategoryForm(request.POST)
        if form.data :
            oldName = form.data['oldName']
            newName = form.data['newName']
            return HttpResponse(CategoryQuery().updateCategory(oldName, newName))
        else :
            return HttpResponseServerError()
    elif request.method == 'GET' :
        return HttpResponseNotAllowed(['POST'])

# category/delete
@csrf_exempt
def category_delete(request) :
    if request.method == 'POST' :
        form = CategoryForm(request.POST) # always no data

        if form.data :
            name = form.data['name']
            return HttpResponse(CategoryQuery().deleteCategory(name))
        else :
            return HttpResponseServerError()
    elif request.method == 'GET' :
        return HttpResponseNotAllowed(['POST'])