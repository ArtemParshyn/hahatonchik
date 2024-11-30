from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from django.db import models

from django.db import models


class ApiUser(AbstractUser):
    ...


class Project(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fio = models.CharField(max_length=255, blank=False)
    stazh = models.CharField(max_length=255, blank=False)
    position = models.CharField(max_length=255, blank=False)
    number = models.CharField(max_length=255, blank=False)
    mail = models.CharField(max_length=255, blank=False)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE, blank=True)
    salary = models.IntegerField(blank=False)
    age = models.IntegerField(blank=False)
    city = models.CharField(max_length=255, blank=False)
    date_of_birth = models.DateField(blank=False)
    is_founder = models.BooleanField(default=False, verbose_name="Нет сверху по вертикали никого")  # Галочка
    zevisit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Зависит от",
    )

    def __str__(self):
        return self.fio
