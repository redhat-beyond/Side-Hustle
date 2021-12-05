from django.db import models
from django.conf import settings
from django.contrib.auth.models import User as DjangoUser


class Role(models.TextChoices):
    HR = 'hr', 'HR'
    STUDENT = 'student', 'Student'


class User(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
        blank=True,
        null=True
    )

    @staticmethod
    def create_user(username, email, password, full_name, role):
        django_user = DjangoUser.objects.create_user(username=username,
                                                     email=email,
                                                     password=password)
        user = User(user=django_user,
                    full_name=full_name,
                    role=role)
        user.save()
        return user

    @staticmethod
    def get_user(username):
        try:
            user = DjangoUser.objects.get(username=username)
        except DjangoUser.DoesNotExist:
            return None
        return user

    def del_user(self):
        try:
            self.user.delete()
        except User.DoesNotExist:
            return False
        return True

    def __str__(self) -> str:
        return self.full_name

    def is_student(self):
        return self.role == Role.STUDENT

    def is_HR(self):
        return self.role == Role.HR
