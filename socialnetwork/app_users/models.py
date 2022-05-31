from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    """Путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>"""
    return f'{instance.nick_name}/avatar/{filename}'


def max_value(image_file):
    """Валидатор для ограничения размера загружаемой картинки"""
    if image_file.size >= 1024 ** 2:
        raise ValueError('Максимальный размер файла 1 Мб')


class Profile(models.Model):
    GENDER_CHOICES = [
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    ]
    avatar = models.ImageField(upload_to=user_directory_path,
                               blank=True,
                               default='../media/avatars/noavatar.jpg',
                               validators=[max_value, FileExtensionValidator([
                                   'jpg',
                                   'jpeg',
                                   'png'],
                                   'Поддерживаются файлы JPG, JPEG и PNG')
                                           ],
                               verbose_name='Аватарка'
                               )
    nick_name = models.ForeignKey(User, max_length=15, default=User, on_delete=models.CASCADE,
                                  verbose_name='Ник')
    name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=15, verbose_name='Фамилия')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='m', verbose_name='Пол')
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    vk_account = models.URLField(verbose_name='Ссылка ВК')
    tg_account = models.CharField(max_length=30, verbose_name='Ссылка Телеграм')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    about = models.TextField(max_length=500, default=None, verbose_name='О себе')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profiles_db'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
