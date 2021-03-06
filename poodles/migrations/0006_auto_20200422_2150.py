# Generated by Django 2.2.10 on 2020-04-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poodles', '0005_image_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='uploaded_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='uploaded_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='document',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
