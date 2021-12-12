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


def create_email(username):
    return f'{username}{DEFAULT_MAIL_EXTENSION}'


@pytest.fixture
def job_1():
    job = Job.create_job(title='Software Engineer',
                         description='Full time software engineer at Wix: Front end',
                         location=DEFAULT_JOB_LOCATION,
                         job_type=JobType.FULL_TIME,
                         company_name=DEFAULT_COMPANY_NAME,
                         post_until='2022-12-23',
                         is_active=True,
                         marked_count=0,
                         apply_link=DEFAULT_APPLY_LINK)
    return job


@pytest.fixture
def job_2():
    job = Job.create_job(title='Software Engineer',
                         description='Part time software engineer at Wix: Back end',
                         location=DEFAULT_JOB_LOCATION,
                         job_type=DEFAULT_JOB_TYPE,
                         company_name=DEFAULT_COMPANY_NAME,
                         post_until='2022-12-23',
                         is_active=True,
                         marked_count=0,
                         apply_link=DEFAULT_APPLY_LINK)
    return job


@pytest.fixture
def user_1() -> User:
    username = 'user1'
    email = create_email(username)
    user1 = User.objects.create_user(username=username,
                                     first_name=DEFAULT_FIRST_NAME,
                                     last_name=DEFAULT_LAST_NAME,
                                     email=email,
                                     password=DEFAULT_VALID_PASSWORD)
    user1.role = DEFAULT_USER_ROLE
    user1.save()
    return user1


@pytest.fixture
def user_2() -> User:
    username = 'user2'
    email = create_email(username)
    user2 = User.objects.create_user(username=username,
                                     first_name=DEFAULT_FIRST_NAME,
                                     last_name=DEFAULT_LAST_NAME,
                                     email=email,
                                     password=DEFAULT_VALID_PASSWORD)
    user2.role = DEFAULT_USER_ROLE
    user2.save()
    return user2


@pytest.fixture
def user_student() -> User:
    username = 'user_student'
    email = create_email(username)
    user_student = User.objects.create_user(username=username,
                                            first_name=DEFAULT_FIRST_NAME,
                                            last_name=DEFAULT_LAST_NAME,
                                            email=email,
                                            password=DEFAULT_VALID_PASSWORD)
    user_student.role = DEFAULT_USER_ROLE
    user_student.save()
    return user_student


@pytest.fixture
def user_HR() -> User:
    username = 'user_HR'
    email = create_email(username)
    user_HR = User.objects.create_user(username=username,
                                       first_name=DEFAULT_FIRST_NAME,
                                       last_name=DEFAULT_LAST_NAME,
                                       email=email,
                                       password=DEFAULT_VALID_PASSWORD)
    user_HR.role = 'HR'
    user_HR.save()
    return user_HR
