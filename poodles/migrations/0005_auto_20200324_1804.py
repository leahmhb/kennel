# Generated by Django 2.2.10 on 2020-03-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poodles', '0004_auto_20200324_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
