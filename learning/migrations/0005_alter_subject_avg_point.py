# Generated by Django 4.1 on 2022-11-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_score_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='avg_point',
            field=models.IntegerField(blank=True),
        ),
    ]
