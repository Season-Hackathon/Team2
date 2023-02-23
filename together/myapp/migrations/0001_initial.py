# Generated by Django 4.0.4 on 2023-02-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=400)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, max_length=500, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Univ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('univ', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='', max_length=10)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
