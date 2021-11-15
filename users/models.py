from django.db import models
from django.conf import settings

#Enums
class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    UNSPECIFIED = 'U', 'Unspecified'

class Role(models.TextChoices):
    EMPLOYER = 'employer', 'Employer'
    EMPLOYEE = 'employee', 'Employee'

#Model Class
class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(
        max_length = 1,
        choices=Gender.choices,
        default=Gender.UNSPECIFIED,
        blank=True, null=True
    )
    role = models.CharField(
        max_length = 10,
        choices=Role.choices,
        default=Role.EMPLOYEE,
        blank=True, null=True
    )
    email = models.EmailField(max_length=200)
    # need to add conditions to the password
    password = models.CharField(max_length=50)

