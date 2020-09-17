from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('brain_indexing', views.brain_indexing, name='brain_indexing'),
    path('known_card/<int:card_id>', views.known_card, name='known_card'),
    path('unknown_card/<int:card_id>', views.unknown_card, name='unknown_card')
]
