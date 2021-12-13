import pytest
from jobs.models import Job, JobType, Location
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
def test_unique_apply_link():
    try:
        job1 = Job.create_job(title='Elecrtical Engineer',
                              description='Part time Elecrtical Enginee at Google: Back end',
                              location=Location.Tel_Aviv,
                              job_type=JobType.PART_TIME,
                              company_name="Google",
                              post_until='2022-12-23',
                              is_active=True,
                              marked_count=0,
                              apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/466701")
        job1.save()
        job1_dup_apply_link = Job.create_job(title='Software Engineer',
                                             description='Full time software engineer at Wix: Back end',
                                             location=Location.Tel_Aviv,
                                             job_type=JobType.FULL_TIME,
                                             company_name='Wix',
                                             post_until='2022-12-23',
                                             is_active=True,
                                             marked_count=0,
                                             apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/466701")
        job1_dup_apply_link.save()
        assert False
    except Exception:
        assert True


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

    def test_get_jobs_by_location(cls, job_1, job_2):
        job1_location = Job.get_job_location(job_1)
        job2_location = Job.get_job_location(job_2)
        out = Job.get_by_location(Location.Tel_Aviv)
        assert job1_location == Location.Tel_Aviv
        assert isinstance(out, QuerySet)
        assert all(isinstance(j, Job) for j in out)
        assert not job1_location == job2_location
        assert set(out) == set([job_1])
        assert not set(out) == set([job_1, job_2])

    def test_get_jobs_by_title(cls, job_1, job_2):
        job1_title = str(job_1)
        job2_title = str(job_2)
        out = Job.get_by_title(job1_title)
        assert isinstance(out, QuerySet)
        assert all(isinstance(j, Job) for j in out)
        assert not job1_title == job2_title
        assert set(out) == set([job_1])
        assert not set(out) == set([job_1, job_2])

    def test_get_jobs_by_title_loc_type(cls, job_1, job_2):
        job1_title = str(job_1)
        job2_title = str(job_2)
        job1_location = Job.get_job_location(job_1)
        job2_location = Job.get_job_location(job_2)
        job1_type = Job.get_job_type(job_1)
        job2_type = Job.get_job_type(job_2)
        out = Job.get_by_three_fields(job1_title, job1_location, job1_type)
        assert isinstance(out, QuerySet)
        assert all(isinstance(j, Job) for j in out)
        assert not job1_title == job2_title
        assert not job1_location == job2_location
        assert not job1_type == job2_type
        assert set(out) == set([job_1])
        assert not set(out) == set([job_1, job_2])
