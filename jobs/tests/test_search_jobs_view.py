import pytest
from jobs.models import Job
from conftest import DEFAULT_JOB_LOCATION, DEFAULT_JOB_TYPE, DEFAULT_COMPANY_NAME


NUM_OF_JOBS = 10


@pytest.fixture
def software_engineer_jobs(user_HR):
    software_engineer_jobs = []
    for i in range(NUM_OF_JOBS):
        software_engineer_job = Job.create_job(
                                publisher=user_HR,
                                title='Software Engineer',
                                description='Part time software engineer at Wix: Back end',
                                location=DEFAULT_JOB_LOCATION,
                                job_type=DEFAULT_JOB_TYPE,
                                company_name=DEFAULT_COMPANY_NAME,
                                post_until='2022-12-23',
                                is_active=True,
                                marked_count=0,
                                apply_link=f'https://www.wix.com/jobs/locations/tel-aviv/positions/s-e/{i}')
        software_engineer_jobs.append(software_engineer_job)
    return software_engineer_jobs


@pytest.fixture
def data_engineer_jobs(user_HR):
    data_engineer_jobs = []
    for i in range(NUM_OF_JOBS):
        data_engineer_job = Job.create_job(
                            publisher=user_HR,
                            title='Data Engineer',
                            description='Part time software engineer at Wix: Back end',
                            location=DEFAULT_JOB_LOCATION,
                            job_type=DEFAULT_JOB_TYPE,
                            company_name=DEFAULT_COMPANY_NAME,
                            post_until='2022-12-23',
                            is_active=True,
                            marked_count=0,
                            apply_link=f'https://www.wix.com/jobs/locations/tel-aviv/positions/d-e/{i}')
        data_engineer_jobs.append(data_engineer_job)
    return data_engineer_jobs


@pytest.fixture
def bad_data_engineer_job_title(data_engineer_jobs):
    return data_engineer_jobs[0].title + 'e'


@pytest.fixture
def data_engineer_job_title(data_engineer_jobs):
    return data_engineer_jobs[0].title


@pytest.fixture
def client_with_student_user(client, user_student):
    client.force_login(user_student)
    return client


@pytest.fixture
def client_with_hr_user(client, user_HR):
    client.force_login(user_HR)
    return client


@pytest.mark.django_db
def test_redirect_unauthenticated_user_when_enter_search_jobs(client, job_1):
    response = client.get('/jobs/search?search_query=')
    assert response.status_code == 302
    assert response.url == '/home/'


@pytest.mark.django_db
def test_hr_user_job_search_by_partial_title(client_with_hr_user, data_engineer_jobs, data_engineer_job_title):
    num_of_data_engineer_jobs = len(data_engineer_jobs)
    assert Job.objects.count() == num_of_data_engineer_jobs

    for i in range(len(data_engineer_job_title)):
        partial_data_engineer_title = data_engineer_job_title[:i]
        response = client_with_hr_user.get(f'/jobs/search?search_query={partial_data_engineer_title}')
        assert response.status_code == 200

        filtered_jobs = response.context['filtered_jobs']
        assert len(filtered_jobs) == num_of_data_engineer_jobs
        assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=partial_data_engineer_title))


@pytest.mark.django_db
def test_hr_user_job_search_by_exact_title(client_with_hr_user,
                                           data_engineer_jobs, data_engineer_job_title, software_engineer_jobs):
    num_of_data_engineer_jobs = len(data_engineer_jobs)
    assert Job.objects.count() == num_of_data_engineer_jobs + len(software_engineer_jobs)

    response = client_with_hr_user.get(f'/jobs/search?search_query={data_engineer_job_title}')
    assert response.status_code == 200

    filtered_jobs = response.context['filtered_jobs']
    assert len(filtered_jobs) == num_of_data_engineer_jobs
    assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=data_engineer_job_title))


@pytest.mark.django_db
def test_hr_user_job_search_by_bad_title(client_with_hr_user, data_engineer_jobs, bad_data_engineer_job_title):
    assert Job.objects.count() == len(data_engineer_jobs)

    response = client_with_hr_user.get(f'/jobs/search?search_query={bad_data_engineer_job_title}')
    assert response.status_code == 200

    filtered_jobs = response.context['filtered_jobs']
    assert len(filtered_jobs) == 0
    assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=bad_data_engineer_job_title))


@pytest.mark.django_db
def test_hr_user_job_search_by_partial_empty_title(client_with_hr_user, data_engineer_jobs, software_engineer_jobs):
    num_of_all_jobs = len(data_engineer_jobs) + len(software_engineer_jobs)
    assert Job.objects.count() == num_of_all_jobs

    empty_title = ''
    response = client_with_hr_user.get(f'/jobs/search?search_query={empty_title}')
    assert response.status_code == 200

    filtered_jobs = response.context['filtered_jobs']
    assert len(filtered_jobs) == num_of_all_jobs
    assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=empty_title))


@pytest.mark.django_db
def test_student_user_job_search_by_partial_title(client_with_student_user,
                                                  data_engineer_jobs, data_engineer_job_title):
    num_of_data_engineer_jobs = len(data_engineer_jobs)
    assert Job.objects.count() == num_of_data_engineer_jobs

    for i in range(len(data_engineer_job_title)):
        partial_data_engineer_title = data_engineer_job_title[:i]
        response = client_with_student_user.get(f'/jobs/search?search_query={partial_data_engineer_title}')
        assert response.status_code == 200

        filtered_jobs = response.context['filtered_jobs']
        assert len(filtered_jobs) == num_of_data_engineer_jobs
        assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=partial_data_engineer_title))


@pytest.mark.django_db
def test_student_user_job_search_by_exact_title(client_with_student_user,
                                                data_engineer_jobs, data_engineer_job_title, software_engineer_jobs):
    num_of_data_engineer_jobs = len(data_engineer_jobs)
    assert Job.objects.count() == num_of_data_engineer_jobs + len(software_engineer_jobs)

    response = client_with_student_user.get(f'/jobs/search?search_query={data_engineer_job_title}')
    assert response.status_code == 200

    filtered_jobs = response.context['filtered_jobs']
    assert len(filtered_jobs) == num_of_data_engineer_jobs
    assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=data_engineer_job_title))


@pytest.mark.django_db
def test_student_user_job_search_by_bad_title(client_with_student_user,
                                              data_engineer_jobs, bad_data_engineer_job_title):
    assert Job.objects.count() == len(data_engineer_jobs)

    response = client_with_student_user.get(f'/jobs/search?search_query={bad_data_engineer_job_title}')
    assert response.status_code == 200

    filtered_jobs = response.context['filtered_jobs']
    assert len(filtered_jobs) == 0
    assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=bad_data_engineer_job_title))


@pytest.mark.django_db
def test_student_user_job_search_by_empty_title(client_with_student_user, data_engineer_jobs, software_engineer_jobs):
    num_of_all_jobs = len(data_engineer_jobs) + len(software_engineer_jobs)
    assert Job.objects.count() == num_of_all_jobs

    empty_title = ''
    response = client_with_student_user.get(f'/jobs/search?search_query={empty_title}')
    assert response.status_code == 200

    filtered_jobs = response.context['filtered_jobs']
    assert len(filtered_jobs) == num_of_all_jobs
    assert set(filtered_jobs) == set(Job.objects.filter(title__icontains=empty_title))
