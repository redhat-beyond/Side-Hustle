from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    HR = 'hr', 'HR'
    STUDENT = 'student', 'Student'


class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def is_student(self) -> bool:
        return self.role == 'Student' or self.role == 'student'

    def is_HR(self) -> bool:
        return self.role == 'HR' or self.role == 'hr'
