# Generated by Django 5.0 on 2023-12-28 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_book_image_alter_profile_user_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookImage',
        ),
    ]
