# Generated by Django 4.1.6 on 2023-02-16 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_alike_app', '0005_userprofile_alter_post_username_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='heartQty',
        ),
        migrations.RemoveField(
            model_name='post',
            name='heartQty',
        ),
    ]