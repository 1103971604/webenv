# Generated by Django 2.2.1 on 2019-05-18 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20190518_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='heroage',
            field=models.IntegerField(verbose_name='年龄'),
        ),
    ]