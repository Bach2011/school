# Generated by Django 4.1 on 2022-11-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='kind',
            field=models.IntegerField(),
        ),
    ]
