# Generated by Django 4.0.4 on 2023-02-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='univ',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d'),
        ),
    ]