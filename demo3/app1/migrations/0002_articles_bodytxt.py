# Generated by Django 2.2.1 on 2019-05-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='bodytxt',
            field=models.TextField(default='', max_length=500),
        ),
    ]
