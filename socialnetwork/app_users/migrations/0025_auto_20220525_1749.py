# Generated by Django 2.2 on 2022-05-25 14:49

import app_users.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0024_auto_20220512_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='../media/avatars/noavatar.jpg', upload_to=app_users.models.user_directory_path, validators=[app_users.models.max_value, django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'], 'Поддерживаются файлы JPG, JPEG и PNG')], verbose_name='Аватарка'),
        ),
    ]
