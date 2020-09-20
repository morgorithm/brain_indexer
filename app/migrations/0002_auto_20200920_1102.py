# Generated by Django 3.1 on 2020-09-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_detail',
        ),
        migrations.AddField(
            model_name='card',
            name='description',
            field=models.CharField(default='defaultValue', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='CardDetail',
        ),
    ]
