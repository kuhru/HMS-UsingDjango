# Generated by Django 3.0.5 on 2020-05-25 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactpage',
            old_name='name',
            new_name='full_name',
        ),
    ]