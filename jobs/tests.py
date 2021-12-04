import pytest
from jobs.models import Job
from django.contrib.auth.models import User

class Role(models.TextChoices):
    HR = 'hr', 'HR'
    STUDENT = 'student', 'Student'
@pytest.fixture
def job_1():
    job = Job.create_job(publisher=User.objects.create_user('Rick', 'Rick@test.com', 'Rick', 'b', Role.HR),
                         title='CS', description='This message needs to cut before this ends', job_type='1',
                         location='1', company_name='WIX',
                         post_until='1994-12-23', is_active=True, marked_count=0,
                         apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/342602")
    return job


def job_2():
    job = Job.create_job(publisher=User.objects.create_user('HR_User', 'HR@test.com', 'HR_password',
                         'John HR', Role.HR),
                         title='Network Deployment Engineer',
                         description='In this role, you will be at the forefront of our efforts.', job_type='2',
                         location='1', company_name='Google',
                         post_until='1994-12-23', is_active=True, marked_count=0,
                         apply_link="https://www.google.com/about/careers/applications/")
    return job
<<<<<<< HEAD


@pytest.mark.django_db
def test_job_create(job_1):
    assert isinstance(job_1, Job)
    assert Job.objects.count() == 1
=======
>>>>>>> a8af8c9 (Add job method and more tests)


# @pytest.mark.django_db
# def test_job_create(job_1):
#     assert isinstance(job_1, Job)
#     assert Job.objects.count() == 1


<<<<<<< HEAD
@pytest.mark.django_db
def test_job_str(job_1):
    assert str(job_1) == job_1.title


@pytest.mark.django_db
def test_job_des_str(job_1):
    assert get_description(job_1) == job_1.description


@pytest.mark.django_db
def test_job_snippet_description(job_1):
    job_des = get_description(job_1)
    assert len(Job.snippet_description(job_1)) <= 28
    assert job_des.endswith("...") == True


@pytest.mark.django_db
def test_delete_job(job_1):
    jobId = job_1.id
    job_1.del_job()
    assert not Job.objects.filter(user=jobId).exists()
=======
# @pytest.mark.django_db
# def test_empty_database():
#     num_of_jobs = Job.objects.all().count()
#     assert num_of_jobs == 0


# @pytest.mark.django_db
# def test_job_str(job_1):
#     assert str(job_1) == job_1.title


# @pytest.mark.django_db
# def test_job_des_str(job_1):
#     assert get_description(job_1) == job_1.description


@pytest.mark.django_db
def test_job_snippet_description(job_1):
    job_des = get_description(job_1)
    print(f'----------------{job_des}-----------------')
    assert len(Job.snippet_description(job_1)) <= 28
    assert job_des.endswith("...") == True


# @pytest.mark.django_db
# def test_delete_job(job_1):
#     jobId = job_1.id
#     job_1.del_job()
#     assert not Job.objects.filter(user=jobId).exists()
>>>>>>> a8af8c9 (Add job method and more tests)
