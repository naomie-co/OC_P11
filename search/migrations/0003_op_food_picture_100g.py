# Generated by Django 3.0.1 on 2020-02-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200211_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='op_food',
            name='picture_100g',
            field=models.URLField(null=True),
        ),
    ]
