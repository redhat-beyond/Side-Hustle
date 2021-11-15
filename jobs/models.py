from django.db import models
from django.utils import timezone
from django.conf import settings

#Enum for Job Types
class JobType(models.TextChoices):
    FULL_TIME = '1', 'Full time'
    PART_TIME = '2', 'Part time'
    INTERNSHIP = '3', 'Internship'

#Jobs Model
class Jobs(models.Model):

    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name='%(class)s_author'
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    job_type = models.CharField(
        max_length = 15,
        choices=JobType.choices,
        default=JobType.PART_TIME,
        blank=True, null=True
    )
    company_name = models.CharField(max_length=255)
    company_description = models.CharField(max_length=255)
    post_until = models.DateField()
    timestamp = models.DateTimeField(default=timezone.now)
