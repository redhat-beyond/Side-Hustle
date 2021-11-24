import pytest
from jobs.models import Jobs
from django.contrib.auth.models import User


@pytest.fixture
def new_job_generator():
    job = Jobs.create_job(publisher=User.objects.create_user('test', 't@test.com', 'test'),
                          title='CS', description='This message needs to cut before this ends', location='TLV',
                          job_type='1', company_name='WIX', company_description='Web',
                          post_until='1994-12-23', is_active=True)
    return job


@pytest.mark.django_db
def test_job_create(new_job_generator):
    count = Jobs.objects.all().count()
    print(count)
    assert Jobs.objects.count() == 1


@pytest.mark.django_db
def test_job_create1():
    count = Jobs.objects.all().count()
    print(count)
    assert count == 0


@pytest.mark.django_db
def test_job_str(new_job_generator):
    print(new_job_generator.__str__)
    print(new_job_generator.title)
    assert str(new_job_generator) == new_job_generator.title


@pytest.mark.django_db
def test_job_snippet_description(new_job_generator):
    assert len(Jobs.snippet_description(new_job_generator)) <= 28
