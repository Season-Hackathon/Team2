# Generated by Django 4.0.4 on 2023-02-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_question_q_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ans',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(default='', max_length=2000),
        ),
    ]