import pytest
from jobs.models import Job, JobType


@pytest.fixture
def create_job_1():
    job = Job.create_job(title='CS', description='This message needs to cut before this ends', location='TLV',
                         job_type=JobType.FULL_TIME, company_name='WIX', company_description='Web',
                         post_until='1994-12-23', is_active=True)
    return job


@pytest.mark.django_db
def test_job_create(create_job_1):
    assert Job.objects.count() == 1


@pytest.mark.django_db
def test_empty_database():
    num_of_jobs = Job.objects.all().count()
    assert num_of_jobs == 0


@pytest.mark.django_db
def test_job_str(create_job_1):
    assert str(create_job_1) == create_job_1.title


@pytest.mark.django_db
def test_job_snippet_description(create_job_1):
    assert len(Job.snippet_description(create_job_1)) <= 28
