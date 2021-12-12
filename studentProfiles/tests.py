import pytest
from studentProfiles.models import StudentProfile, University
from users.models import User
from jobs.models import Job, Location, JobType


# Temp fixtures - all these fixtures should be in contests.py file

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
def job_1():
    job = Job.create_job(title='Software Engineer', description='Full time software engineer at Wix: Front end',
                         location=Location.Tel_Aviv,
                         job_type=JobType.FULL_TIME, company_name='WIX',
                         post_until='2022-12-23', is_active=True, marked_count=0,
                         apply_link="https://www.wix.com/jobs/locations/tel-aviv/positions/342602")
    return job


@pytest.mark.django_db
def test_create_student_profile(user_1, job_1):

    student_profile = StudentProfile(user=user_1,
                                     university=University.Reichman_University,
                                     graduation_date='2022-12-23')
    student_profile.save()
    student_profile.marked_jobs.add(job_1)

    assert isinstance(student_profile, StudentProfile)
    assert StudentProfile.objects.count() == 1
