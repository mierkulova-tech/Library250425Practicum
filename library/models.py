from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20, help_text="First name of the author", verbose_name="Имя автора")
    last_name = models.CharField(max_length=50, help_text="Last name of the author", verbose_name="Фамилия автора")
    birthday = models.DateField(verbose_name="Дата рождения")
    profile =  models.URLField(blank=True, null=True, verbose_name="Ссылка на соцсеть")
    deleted = models.BooleanField(default=False, help_text="Если галочка включена автор удален", verbose_name="Профиль удален")
    rating = models.FloatField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(10)],
        default=0,
        verbose_name="рейтинг автора"
    )

    def __str__(self):
        return f"{self.last_name[0]}.{self.first_name}"

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    publication_date = models.DateField(blank=True, null=True, verbose_name="дата публикации")
    author = models.ForeignKey(
        "Author",
        on_delete=models.SET_NULL,
        null=True,
        related_name="books"
    )

    def __str__(self):
        return f"{self.title} --{self.author.last_name if self.author else 'NONAME'}"