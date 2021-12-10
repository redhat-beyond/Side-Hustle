import pytest
from users.models import User
from jobs.models import Job, JobType, Location

DEFAULT_VALID_PASSWORD = 'hard.password'
DEFAULT_MAIL_EXTENSION = '@redhat.com'
DEFAULT_USER_ROLE = 'Student'
DEFAULT_FIRST_NAME = 'first_name'
DEFAULT_LAST_NAME = 'last_name'
DEFAULT_JOB_LOCATION = Location.Tel_Aviv
DEFAULT_COMPANY_NAME = 'Wix'
DEFAULT_APPLY_LINK = 'https://www.wix.com/jobs/locations/tel-aviv/positions/342602'
DEFAULT_JOB_TYPE = JobType.PART_TIME


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


@pytest.fixture
def user_1() -> User:
    user1 = User.objects.create_user(username='user1',
                                     first_name='first_name',
                                     last_name='last_name',
                                     email='email',
                                     password='password1')
    user1.role = 'Student'
    user1.save()
    return user1


@pytest.fixture
def user_2() -> User:
    user2 = User.objects.create_user(username='user2',
                                     first_name='first_name',
                                     last_name='last_name',
                                     email='email',
                                     password='password2')
    user2.role = 'Student'
    user2.save()
    return user2


@pytest.fixture
def create_user_student() -> User:
    user_student = User.objects.create_user(username='user_student',
                                            first_name='first_name',
                                            last_name='last_name',
                                            email='email',
                                            password='password1')
    user_student.role = 'Student'
    user_student.save()
    return user_student


@pytest.fixture
def create_user_HR() -> User:
    user_HR = User.objects.create_user(username='user_HR',
                                       first_name='first_name',
                                       last_name='last_name',
                                       email='email',
                                       password='password1')
    user_HR.role = 'HR'
    user_HR.save()
    return user_HR
