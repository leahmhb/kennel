# Generated by Django 2.2.10 on 2020-03-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poodles', '0003_document_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
