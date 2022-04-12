from django.db import models
from userapp.models import User


class Project(models.Model):
    name = models.CharField(verbose_name="Название заметки", max_length=128)
    users = models.ManyToManyField(User, verbose_name="Пользователи")
    repository = models.URLField(verbose_name="Ссылка на репозиторий", blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, verbose_name="Название заметки", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст заметки")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # auto_now_add и auto_now - опции  для автоматического создания и обновления даты и времени.
    creator = models.ForeignKey(User, verbose_name="Пользователь создавший заметку", on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name="Статус активности", default=True)
