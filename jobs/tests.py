import pytest
from jobs.models import Job, JobType, Location


@pytest.fixture
def job_1():
    job = Job.create_job(title='Software Engineer', description='Full time software engineer at Wix: Front end',
                         location=Location.Tel_Aviv,
                         job_type=JobType.FULL_TIME, company_name='WIX',
                         post_until='2022-12-23', is_active=True, marked_count=0,
                         apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/342602")
    return job


@pytest.fixture
def job_2():
    job = Job.create_job(title='Software Engineer', description='Part time software engineer at Wix: Back end',
                         location=Location.Tel_Aviv,
                         job_type=JobType.PART_TIME, company_name='WIX',
                         post_until='2022-12-23', is_active=True, marked_count=0,
                         apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/230603")
    return job


@pytest.mark.django_db
def test_job_create(job_1):
    assert isinstance(job_1, Job)
    assert Job.objects.count() == 1


@pytest.mark.django_db
def test_empty_database():
    num_of_jobs = Job.objects.all().count()
    assert num_of_jobs == 0


@pytest.mark.django_db
def test_job_str(job_1):
    assert str(job_1) == job_1.title


@pytest.mark.django_db
def test_job_des_str(job_1):
    assert Job.get_description(job_1) == job_1.description


@pytest.mark.django_db
def test_job_snippet_description(job_1):
    job_des = Job.snippet_description(job_1)
    assert len(job_des) <= 28
    assert job_des.endswith("...")


@pytest.mark.django_db
def test_del_job(job_1):
    jobId = job_1.id
    job_1.delete()
    assert not Job.objects.filter(id=jobId).exists()
