# Generated by Django 2.2.1 on 2019-05-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.CharField(choices=[(1, '男'), (2, '女')], max_length=10),
        ),
    ]
