from django.db import models


# Enum for Job Types
class JobType(models.TextChoices):
    FULL_TIME = '1', 'Full time'
    PART_TIME = '2', 'Part time'
    INTERNSHIP = '3', 'Internship'


# Jobs Model
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    job_type = models.CharField(
        max_length=15,
        choices=JobType.choices,
        default=JobType.PART_TIME,
        blank=True, null=True
    )
    company_name = models.CharField(max_length=255)
    company_description = models.CharField(max_length=255)
    post_until = models.DateField()
    is_active = models.BooleanField()

    # Function to create a new job
    @classmethod
    def create_job(cls, title, description, location, job_type, company_name,
                   company_description, post_until, is_active):
        job = cls(title=title, description=description, location=location,
                  job_type=job_type, company_name=company_name,
                  company_description=company_description, post_until=post_until, is_active=is_active)
        job.save()
        return job

    # Function to reduce the length of description
    def snippet_description(self):
        return self.description[:25] + '...'

    # Jobs title to string - return the title of the job
    def __str__(self) -> str:
        return self.title
