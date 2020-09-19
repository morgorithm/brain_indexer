from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .query import *
from .forms import *

# Create your views here.
GET_METHOD_DISABLED = "Get Method is Not Allowed"

# category/read
def category_read(request, name) :
    if request.method == 'POST' :
        data = CategoryQuery().readCategory(name)
        json = serializers.serialize('json', data)

        return HttpResponse(json, content_type="text/json-comment-filtered")
    elif request.method == 'GET' :
        return HttpResponse(GET_METHOD_DISABLED)

# category/create
def category_create(request, name) :
    if request.method == 'POST' :
        return HttpResponse(CategoryQuery().createCategory(name))
    elif request.method == 'GET' :
        return HttpResponse(GET_METHOD_DISABLED)

# category/update
def category_update(request, oldName, newName) :
    if request.method == 'POST' :
        return HttpResponse(CategoryQuery().updateCategory(oldName, newName))
    elif request.method == 'GET' :
        return HttpResponse(GET_METHOD_DISABLED)

# category/delete
def category_delete(request) :
    if request.method == 'POST' :
        form = CategoryForm(request.POST) # always no data
        
        return HttpResponse("Test")
        # return HttpResponse(CategoryQuery().deleteCategory(name))
    elif request.method == 'GET' :
        return HttpResponse(GET_METHOD_DISABLED)