# Generated by Django 4.1 on 2022-11-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_alter_subject_avg_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='point',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='avg_point',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
