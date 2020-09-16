from django.contrib import admin

from .models import Card, CardDetail, Category


admin.site.register(Card)
admin.site.register(CardDetail)
admin.site.register(Category)
