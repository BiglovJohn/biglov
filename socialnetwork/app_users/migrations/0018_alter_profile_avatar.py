# Generated by Django 3.2.5 on 2022-05-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0017_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default=None, upload_to='media/avatars', verbose_name='Аватарка'),
        ),
    ]
