# Generated by Django 2.0.1 on 2018-01-06 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_itle',
            new_name='album_title',
        ),
    ]
