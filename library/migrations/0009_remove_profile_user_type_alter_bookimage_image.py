# Generated by Django 5.0 on 2023-12-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_profile_user_bio_profile_user_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='image',
            field=models.ImageField(upload_to='images/user_images'),
        ),
    ]
