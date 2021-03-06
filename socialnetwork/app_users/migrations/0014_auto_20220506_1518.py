# Generated by Django 3.2.5 on 2022-05-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0013_auto_20220506_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.CharField(default=None, max_length=1000, verbose_name='О себе'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=2, upload_to='', verbose_name='Аватарка'),
            preserve_default=False,
        ),
    ]
