# Generated by Django 3.2.5 on 2022-05-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0011_alter_profile_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nick_name',
            field=models.CharField(max_length=15, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tg_account',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Ссылка Телеграм'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vk_account',
            field=models.URLField(blank=True, default=None, verbose_name='Ссылка ВК'),
        ),
    ]