from django.db import models
from django.conf import settings
from jobs.models import Job


# Student Profile Model
class StudentProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name='%(class)s_author'
    )
    university = models.CharField(max_length=255)
    graduation_date = models.DateField()
    marked_jobs = models.ManyToManyField(Job)
