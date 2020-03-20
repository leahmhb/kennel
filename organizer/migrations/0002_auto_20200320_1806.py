# Generated by Django 2.2.7 on 2020-03-20 18:06

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kennel',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from=['last_name', 'first_name', 'mi'], unique=True),
        ),
    ]