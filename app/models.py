from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=64, unique=True)
    total = models.IntegerField(default=0)

    class Meta:
        db_table = 'categories'

class Card(BaseModel):
    name = models.CharField(max_length=64, unique=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False)
    description = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'cards'