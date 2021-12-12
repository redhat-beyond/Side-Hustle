from django.db import models
# from django.conf import settings
from jobs.models import Job
from users.models import User


class University(models.TextChoices):
    Reichman_University = 'RU', 'Reichman University'
    Technion_University = 'TE', "Technion University"
    Hebrew_University = 'HU', 'Hebrew University'
    Tel_Aviv_University = 'TA', 'Tel Aviv University'
    Beer_Sheva_University = 'BS', "Be'er Sheva University"
    Unknown = 'UN', 'Unknown'


# Student Profile Model
class StudentProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='%(class)s_author'
    )
    university = models.CharField(max_length=255)
    graduation_date = models.DateField()
    marked_jobs = models.ManyToManyField(Job)
