# Generated by Django 5.0 on 2023-12-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
    ]