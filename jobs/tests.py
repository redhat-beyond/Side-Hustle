import pytest
from jobs.models import Job
from django.contrib.auth.models import User


@pytest.fixture
def new_job_generator():
    job = Job.create_job(publisher=User.objects.create_user('test_username', 't@test.com', 'test_password',
                         'test_full_name', 'HR'),
                         title='CS', description='This message needs to cut before this ends', job_type='1',
                         location='1', company_name='WIX',
                         post_until='1994-12-23', is_active=True, marked_count=0,
                         apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/342602")
    return job


@pytest.mark.django_db
def test_job_create(new_job_generator):
    assert Job.objects.count() == 1


@pytest.mark.django_db
def test_empty_database():
    num_of_jobs = Job.objects.all().count()
    assert num_of_jobs == 0


@pytest.mark.django_db
def test_job_str(new_job_generator):
    assert str(new_job_generator) == new_job_generator.title


@pytest.mark.django_db
def test_job_snippet_description(new_job_generator):
    assert len(Job.snippet_description(new_job_generator)) <= 28
