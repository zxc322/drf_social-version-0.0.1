# Generated by Django 4.1 on 2022-08-20 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_postlike_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]
