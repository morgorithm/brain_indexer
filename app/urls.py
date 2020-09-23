from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('card', views.CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('random', views.getRandomCard),
]   