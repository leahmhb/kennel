# Generated by Django 2.2.10 on 2020-03-24 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poodles', '0002_auto_20200324_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('poodle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='poodles_images', to='poodles.Poodle', verbose_name='Poodle')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('poodle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='poodles_documents', to='poodles.Poodle', verbose_name='Poodle')),
            ],
        ),
    ]
