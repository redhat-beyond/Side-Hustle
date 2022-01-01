import pytest
from users.models import User, Role
from jobs.models import Job, JobType, Location

DEFAULT_VALID_USERNAME = 'cool_name'
DEFAULT_VALID_PASSWORD = 'hard.password'
DEFAULT_MAIL_EXTENSION = '@redhat.com'
DEFAULT_VALID_MAIL = DEFAULT_VALID_USERNAME + DEFAULT_MAIL_EXTENSION
DEFAULT_USER_ROLE = Role.STUDENT
DEFAULT_FIRST_NAME = 'first_name'
DEFAULT_LAST_NAME = 'last_name'
DEFAULT_JOB_LOCATION = Location.Tel_Aviv
DEFAULT_COMPANY_NAME = 'Wix'
DEFAULT_APPLY_LINK = 'https://www.wix.com/jobs/locations/tel-aviv/positions/342602'
DEFAULT_JOB_TYPE = JobType.PART_TIME


def create_email(username):
    return f'{username}{DEFAULT_MAIL_EXTENSION}'


def create_invalid_objects_data(valid_objects_data, invalid_field, invalid_values):
    invalid_objects = []
    for invalid_value in invalid_values:
        invalid_user_data = valid_objects_data.copy()
        invalid_user_data[invalid_field] = invalid_value
        invalid_objects.append(invalid_user_data)
    return invalid_objects


@pytest.fixture
def invalid_emails():
    invalid_emails = [
        '@gmail.com',
        'w@gmailcom',
        's@gmail.',
        'ddddgmail.com'
    ]
    return invalid_emails


@pytest.fixture
def invalid_usernames():
    invalid_usernames = [
        'shay#',
        'sha,y',
        'sha&',
        ''
    ]
    return invalid_usernames


@pytest.fixture
def invalid_passwords():
    invalid_passwords = [
        '1234567890',
        'abcdefg',
        ''
    ]
    return invalid_passwords


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
def valid_user_data():
    user_data = {'first_name': DEFAULT_FIRST_NAME,
                 'last_name': DEFAULT_LAST_NAME,
                 'email': DEFAULT_VALID_MAIL,
                 'role': DEFAULT_USER_ROLE,
                 'username': DEFAULT_VALID_USERNAME,
                 'password1': DEFAULT_VALID_PASSWORD,
                 'password2': DEFAULT_VALID_PASSWORD}
    return user_data


@pytest.fixture
def valid_student_data(valid_user_data):
    student_data = valid_user_data.copy()
    student_data['role'] = Role.STUDENT
    return student_data


@pytest.fixture
def valid_hr_data(valid_user_data):
    HR_data = valid_user_data.copy()
    HR_data['role'] = Role.HR
    return HR_data


@pytest.fixture
def user_data_with_invalid_passwords(valid_user_data, invalid_passwords):
    invalid_user_data = create_invalid_objects_data(valid_objects_data=valid_user_data,
                                                    invalid_field='password1',
                                                    invalid_values=invalid_passwords)
    return invalid_user_data


@pytest.fixture
def user_data_with_non_matching_password(valid_user_data):
    invalid_user_data = valid_user_data.copy()
    invalid_user_data['password2'] = invalid_user_data['password1'] + '0'
    return invalid_user_data


@pytest.fixture
def user_data_with_invalid_emails(valid_user_data, invalid_emails):
    invalid_users = create_invalid_objects_data(valid_objects_data=valid_user_data,
                                                invalid_field='email',
                                                invalid_values=invalid_emails)
    return invalid_users


@pytest.fixture
def user_data_with_invalid_usernames(valid_user_data, invalid_usernames):
    invalid_users = create_invalid_objects_data(valid_objects_data=valid_user_data,
                                                invalid_field='username',
                                                invalid_values=invalid_usernames)
    return invalid_users


@pytest.fixture
def job_1(user_HR):
    job = Job.create_job(publisher=user_HR, title='Software Engineer',
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
def job_2(user_HR):
    job = Job.create_job(publisher=user_HR, title='Software Engineer',
                         description='Part time software engineer at Wix: Back end',
                         location=DEFAULT_JOB_LOCATION,
                         job_type=DEFAULT_JOB_TYPE,
                         company_name=DEFAULT_COMPANY_NAME,
                         post_until='2022-12-23',
                         is_active=True,
                         marked_count=0,
                         apply_link=DEFAULT_APPLY_LINK)
    return job
