from django.db import models
from jobs.models import Job, User


# Student Profile Model
class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    university = models.CharField(max_length=255)
    graduation_date = models.DateField()
    marked_jobs = models.ManyToManyField(Job)

    def __str__(self) -> str:
        return str(self.user)
