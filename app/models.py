from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class Category(BaseModel):
    objects = models.Manager()
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'categories'


class CardDetail(BaseModel):
    description = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'card_details'


class Card(BaseModel):
    name = models.CharField(max_length=64, unique=True, null=False)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=False)
    card_detail = models.ForeignKey(
        CardDetail, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'cards'
