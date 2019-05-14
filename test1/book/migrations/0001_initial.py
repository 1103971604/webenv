# Generated by Django 2.2.1 on 2019-05-14 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('bpub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='heroinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heroname', models.CharField(max_length=30)),
                ('heroage', models.IntegerField(max_length=5)),
                ('hgender', models.BooleanField(default=True)),
                ('nbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo')),
            ],
        ),
    ]
