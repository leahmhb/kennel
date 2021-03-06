# Generated by Django 2.2.10 on 2020-03-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poodles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.CharField(blank=True, choices=[('CL', 'Class'), ('CO', 'Contract'), ('RE', 'Registration'), ('TT', 'Title')], max_length=255),
        ),
        migrations.AddField(
            model_name='poodle',
            name='color',
            field=models.CharField(choices=[('BL', 'Black'), ('BU', 'Blue'), ('MP', 'Multi/Parti'), ('U', 'Unknown'), ('WH', 'White')], default='U', max_length=2, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='poodle',
            name='sex',
            field=models.CharField(choices=[('F', 'Bitch'), ('M', 'Dog')], default=1, max_length=1, verbose_name='Sex'),
            preserve_default=False,
        ),
    ]
