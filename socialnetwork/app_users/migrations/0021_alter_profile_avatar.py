# Generated by Django 3.2.5 on 2022-05-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0020_auto_20220508_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='../media/avatars/noavatar.jpg', help_text=None, upload_to='avatars/', verbose_name='Аватарка'),
        ),
    ]