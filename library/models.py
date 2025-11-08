from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    profile = models.URLField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    rating = models.FloatField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
        default=0
    )

    def __str__(self):
        return f"{self.last_name[0]}. {self.first_name}"

"""Обновите уже существующую модель Author дополнительными полями:
Профиль: ссылка на личную страницу автора, может быть не указана
Удалён: поле, которое позволит смотреть удалён ли этот автор из базы всех авторов.
По умолчанию все авторы активны
Рейтинг: позволит отсматривать рейтинг популярности авторов, от 1 до 10"""