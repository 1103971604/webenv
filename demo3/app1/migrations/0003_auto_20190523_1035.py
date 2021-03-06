# Generated by Django 2.2.1 on 2019-05-23 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_articles_bodytxt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='pags',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='Readnum',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='bodytxt',
            field=models.TextField(default='', max_length=500, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Category', verbose_name='文章类别'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='pag',
            field=models.ManyToManyField(to='app1.Pags', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='pags',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标签'),
        ),
    ]
