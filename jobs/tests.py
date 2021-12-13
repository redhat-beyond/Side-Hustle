import pytest
from jobs.models import Job, JobType
from django.db.models.query import QuerySet


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


@pytest.mark.django_db
def test_get_job_type(job_1):
    assert Job.get_job_type(job_1) == job_1.job_type


@pytest.mark.django_db
class TestJob:
    def test_get_all_jobs(cls, job_1, job_2):
        out = Job.get_all_jobs()
        assert isinstance(out, QuerySet)
        assert all(isinstance(j, Job) for j in out)
        assert set(out) == set([job_1, job_2])

    def test_get_full_time_jobs(cls, job_1, job_2):
        job1_type = Job.get_job_type(job_1)
        job2_type = Job.get_job_type(job_2)
        out = Job.get_by_type(JobType.FULL_TIME)
        assert job1_type == JobType.FULL_TIME
        assert isinstance(out, QuerySet)
        assert all(isinstance(j, Job) for j in out)
        assert not job1_type == job2_type
        assert set(out) == set([job_1])
        assert not set(out) == set([job_1, job_2])
