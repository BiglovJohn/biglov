# Generated by Django 3.2.5 on 2022-05-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0009_auto_20220506_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(max_length=2000, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vk_account',
            field=models.URLField(blank=True, verbose_name='Ссылка ВК'),
        ),
    ]
